<?php 
$dbServername="127.0.0.1";

$dbUsername = "root";
$dbPassword="rootpass";


$dbName = "banco";

function runQuery($conn,$sql){
    if (mysqli_query($conn, $sql)) {
       echo "Query sucessfully<br>";
    } 
    else {
       echo "Error running query: " . mysqli_error($conn)."<br>";
    }


}


$conn = mysqli_connect($dbServername,$dbUsername,$dbPassword);
// Check connection




if($conn === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
 
// Print host information
echo "Connect Successfully. Host info: " ;


$sql = "CREATE DATABASE ".$dbName;
runQuery($conn,$sql);


$sql = "USE ".$dbName;
runQuery($conn,$sql);

$sql = "create table users (
	id  int(11) not null PRIMARY KEY AUTO_INCREMENT,
	username varchar(40) not null,
	password varchar(100) not null,
	email varchar(100) not null
	
);
";
runQuery($conn,$sql);

$sql = "create table posts (
	id  int(11) not null PRIMARY KEY AUTO_INCREMENT,
	poster varchar(40) not null,
	titulo varchar(100) not null,
	conteudo varchar(6000) not null,
	date int(8) not null,
	likes int(11) not null

);
";
runQuery($conn,$sql);


mysqli_close($conn);

?>
