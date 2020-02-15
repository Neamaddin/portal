function ConfirmDelete(){
var resultActionUser = confirm('Вы действительно хотите удалить этот документ?');
if(resultActionUser){return true;}
else{return false;}
}