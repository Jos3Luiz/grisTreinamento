<?php 
$dbServername="127.0.0.1";
$dbUsername = "root";
$dbPassword="rootpass";


$dbName = "banco";

$conn = mysqli_connect($dbServername,$dbUsername,$dbPassword,$dbName);
// Check connection
if($conn === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
 
// Print host information
echo "Connect Successfully. Host info: " . mysqli_get_host_info($link);
 




?>
