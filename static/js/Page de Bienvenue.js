// function revealOnScroll(){
//     const revealElements = document.querySelectorAll('.d1');
//     revealElements.forEach((element)=> {
//         if (isElementInViewport(element)){
//             element.classList.add('visible');
//         }
//     });
// }

// window.addEventListener('scroll', revealOnScroll);

// revealOnScroll();



function revealOnload(){
    const revealElements = document.querySelectorAll('.d1');
    revealElements.forEach((element, index)=> {
        setTimeout(() => {
            element.classList.add('visible');
        },index * 300);
    });
}

window.addEventListener('load', revealOnScroll);

revealOnScroll();