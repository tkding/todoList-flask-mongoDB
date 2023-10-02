from application import app, db
from flask import render_template, request, redirect, url_for, flash
from application.forms import ItemForm
from datetime import datetime
from bson import ObjectId

@app.route("/")
def index():
    todos = []
    for todo in db.items.find().sort("date_created", -1):
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%m/%d/%Y, %H:%M:%S")
        todos.append(todo)    
    
    
    return render_template("index.html", todos=todos)

@app.route("/create", methods=["POST", "GET"])
def create():
    form = ItemForm()
    
    if request.method == "POST" and form.validate_on_submit():
        form = ItemForm(request.form)
        todo_title = form.title.data
        todo_description = form.description.data
        todo_completed = form.completed.data
        
        db.items.insert_one({
            "title": todo_title, 
            "description": todo_description, 
            "completed": todo_completed,
            "date_created": datetime.utcnow()
        })
        flash(f"Todo item {todo_title} has been created successfully!", category="success")
        return redirect(url_for("index"))
    
    if form.errors != {}: # If there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f"There was an error with creating a user: {err_msg}", category="danger")
            
    if request.method == "GET":
        return render_template("create.html", form=form)
            
    return render_template("create.html", form=form)

@app.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    todo = db.items.find_one({"_id": ObjectId(id)}) # returns a dictionary
    form = ItemForm()
    
    if request.method == "GET":
        form.title.data = todo.get("title", None)
        form.description.data = todo.get("description", None)
        form.completed.data = todo.get("completed", None)
        return render_template("create.html", form=form)
    
    if request.method == "POST" and form.validate_on_submit():
        form = ItemForm(request.form)
        todo_title = form.title.data
        todo_description = form.description.data
        todo_completed = form.completed.data
        
        db.items.update_one({"_id": ObjectId(id)}, {
            "$set": {
                "title": todo_title, 
                "description": todo_description, 
                "completed": todo_completed,
                "date_created": datetime.utcnow()
            }
        })
        flash(f"Todo item {todo_title} has been updated successfully!", category="success")
        return redirect(url_for("index"))
    
    if form.errors != {}: 
        for err_msg in form.errors.values():
            flash(f"There was an error with updating a user: {err_msg}", category="danger")
    
    return render_template("create.html", form=form)

@app.route("/delete/<id>", methods=["POST", "GET"])
def delete(id):
    todo = db.items.find_one_and_delete({"_id": ObjectId(id)})
    flash(f"Todo item {todo['title']} has been deleted successfully!", category="success")
    return redirect(url_for("index"))