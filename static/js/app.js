// rest countries api js
document.addEventListener('DOMContentLoaded', () => {
    // const select = document.querySelector('#countries');
    const select = document.getElementById('countries');
  
    fetch('https://restcountries.com/v2/all').then(res => {
      return res.json();
    }).then(data => {
        let output = "";
      data.forEach(country => {
        output += `<option value="${country.name}">${country.name}</option>`;
      })
      select.innerHTML = output;
    }).catch(err => {
      console.log(err);
    })
  })


  // Font awesome js
AOS.init();


// For tooltip msg js
// tippy('#myButton', {
//     content: 'My tooltip!',
//   });