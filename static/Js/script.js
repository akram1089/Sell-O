console.log('Hi there ');
var x=2
function add_table(){
var tab=document.getElementById('tab')
var row=tab.insertRow()
var cell1=row.insertCell(0)
var cell2=row.insertCell(1)
var cell3=row.insertCell(2)
var cell4=row.insertCell(3)
var cell5=row.insertCell(4)
var cell6=row.insertCell(5)
var cell7=row.insertCell(6)
var cell8=row.insertCell(7)
var cell9=row.insertCell(8)
cell1.innerHTML= x++
cell2.innerHTML= ` <input
type='text'
class='form-control'
name='pname'
required
placeholder='Product name:'
/>`

cell3.innerHTML= `<input
type="text"
class="form-control"
name="mrp"
required
placeholder=" MRP:"
/>`
cell4.innerHTML= `<input
type="text"
class="form-control"
name="dprice"
required
placeholder="Discount Price:"
/>`
cell5.innerHTML= `<input
type="text"
class="form-control"
name="bname"
required
placeholder="Brand Name:"
/>`
cell6.innerHTML= ` <input
type="text"
class="form-control"
name="vender"
required
placeholder="Vender Name:"
/>`
cell7.innerHTML= ` <select
class="form-select"
id="select"
name="pcategory"
aria-label="Default select example"
>
<option value="Not chosen" selected>Product Category</option>
<option>Brand New</option>
<option>Used</option>
<option>Refurbished</option>
</select>`
cell8.innerHTML= ` <textarea
class="form-control"
placeholder="products details"
id="exampleFormControlTextarea1"
rows="1"
name="pdescription"
></textarea>`
cell9.innerHTML= `<input
class="form-control"
type="file"
id="formFile"
name="product_image"
/>`

    
}

       // Wrap every letter in a span
       var textWrapper = document.querySelector('.ml11 .letters');
       textWrapper.innerHTML = textWrapper.textContent.replace(/([^\x00-\x80]|\w)/g, "<span class='letter'>$&</span>");
       
       anime.timeline({loop: true})
         .add({
           targets: '.ml11 .line',
           scaleY: [0,1],
           opacity: [0.5,1],
           easing: "easeOutExpo",
           duration: 700
         })
         .add({
           targets: '.ml11 .line',
           translateX: [0, document.querySelector('.ml11 .letters').getBoundingClientRect().width + 10],
           easing: "easeOutExpo",
           duration: 700,
           delay: 100
         }).add({
           targets: '.ml11 .letter',
           opacity: [0,1],
           easing: "easeOutExpo",
           duration: 600,
           offset: '-=775',
           delay: (el, i) => 34 * (i+1)
         }).add({
           targets: '.ml11',
           opacity: 0,
           duration: 1000,
           easing: "easeOutExpo",
           delay: 1000
         });