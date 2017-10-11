<!DOCTYPE html>
<?php 
if (isset($_POST['send'])) {
    $to = 'evan.pringle1@gmail.com';
    $subject = 'Feedback from my site';
    $message = 'Name: ' . $_POST['name'] . "\r\n\r\n";
    $message .= 'Email: ' . $_POST['email'] . "\r\n\r\n";
    $message .= 'Comments: ' . $_POST['comments'];
    echo $message;
}
?>