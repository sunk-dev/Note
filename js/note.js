user={}
console.log(user);
user.name='john';
console.log(user);
user.surname='Smith';
console.log(user);
user.name='Pete';
console.log(user);
delete user.name;
console.log(user);


//----------------------------------------//
const isEmpty=(obj)=>{
    for(let key in obj){
        return false;
    }
    return true;
};
// 객체는 length 적용안됨.
let schedule={};
console.log(schedule.length);
console.log(isEmpty(schedule));
schedule["8:30"] = "get up";
console.log(isEmpty(schedule));

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
  };

let total=0;
// 프로퍼티 꺼내는 차이 dict.key dict[key] 적어두기
for (let key in salaries){
    total+=salaries[key];
}
console.log(total);

// 함수 호출 전
let menu = {
    width: 200,
    height: 300,
    title: "My menu"
  };

const multiplyNumeric=(menu)=>{
    for (let key in menu){
        if (typeof menu[key]==='number'){
            menu[key]*=2;
        }
    }
};

multiplyNumeric(menu);
console.log(menu);  




