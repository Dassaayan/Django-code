var d = new Date();
document.getElementById("demo2").innerHTML = d.getDate();
function changable() {
	// body...
	document.getElementById('Demo').innerHTML='Your mind changed'
	};
function Notchange(){
	document.getElementById('Demo').innerHTML="A paragraph that change your mind"
};
document.write("How is it?");
alert("Feel comfortable ???");
var array=["Hi","I","am","there"]
document.getElementById("demo1").innerHTML=array[0];
var person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    document.getElementById("demo").innerHTML=this.firstName + " " + this.lastName;
  }    
};
function validateForm() {
  var x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }
};
person.fullName();