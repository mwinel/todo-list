// Create todo item by clicking the Add Item button
newItem = () => {
    const inputValue = document.getElementById("todoItem").value;
    const listItem = document.createElement("LI");
    const btn = document.createElement("BUTTON");
    const text = document.createTextNode(inputValue);
    btn.appendChild(text);
    listItem.appendChild(text);
    if (inputValue === '') {
        alert("Field cannot be empty")
    } else {
        document.getElementById("todoItems").appendChild(listItem);
    }
    document.getElementById("todoItem").value = "";

    // Create a delete button and append it to the todo item
    const span = document.createElement("SPAN");
    const deleteItem = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(deleteItem);
    listItem.appendChild(span);

    // Delete a todo item from a todo list
    let close = document.getElementsByClassName("close");
    for (let i = 0; i < close.length; i++) {
        close[i].onclick = function() {
            let div = this.parentElement;
            div.style.display = "none";
        }
    }
}

// Check a todo item as done
const todoList = document.querySelector("ul");
todoList.addEventListener("click", (done) => {
    if (done.target.tagName === "LI") {
        done.target.classList.toggle("done");
    }
}, false);
