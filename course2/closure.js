var a = 10;
let closure = () => {console.log(a)};
closure(a)
a = 20;
closure(a)