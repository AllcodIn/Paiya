<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/CreateEvent.css">
    <title>Create Event Page</title>
</head>
<body>
<style>
    /* *{
    margin: 0;
    padding: 0;
    font-family: sans-serif;
    box-sizing: border-box;
}
body{
}
form{
    display: flex;
    flex-direction: column;
    border: 1px solid black;
    margin-left: 50px;
}
input{
    width: 50%;
    height: 4vh;
    border-radius: 8px;
    /* border: 1px solid palevioletred; 
}
input::placeholder{
    border: 1px solid palevioletred;
} */

    *{
    margin: 0;
    padding: 0;
    font-family: sans-serif;
    box-sizing: border-box;
}
body{
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f2f2f2;
   
}
form{
    margin-top: 8%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    border: 1px solid black;
    border-radius: 8px;
    width: max-content;
    height: 40vw;
}
.left-side{
    margin-top: 8%;
    display: flex;
    background-color: sandybrown;
    justify-content: center;
    align-items: center;
    gap: 20px;
    border: 1px solid black;
    border-radius: 8px;
    width: max-content;
    height: 40vw;
}
input,
select{
    width: 60%;
    height: 5vh;
    border: transparent;
    border-radius: 8px;
}
.sub{
    background-color: palevioletred;
    font-size: x-large;
    color: aliceblue;
    border: transparent;
}
.left-side,
.right-side{
    width: 40%;
    height: 40vw;
    border: 1px solid black;
}
.right-side{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 40%;
    height: 40vw;
    border: 1px solid black;
    background-color: salmon;
}
.upload{
    width: 70%;
    height: 40%;
    border: 1px solid black;
    background-color: palevioletred;
}
</style>

    <!-- <form action="">
        <input type="text" name="" id="" placeholder="Event Name">
        <input type="text" name="" id="" placeholder="">
        <input type="date" name="" id="" placeholder="Date">
        <input type="time" name="" id="" placeholder="hours">
        <input type="text" name="" id="" placeholder="Location">
        <input type="date" name="" id="" placeholder="">
        <input type="tel" name="" id="" placeholder="Tel">
         Here I want to put an upload area 
        <input type="image" src="" alt="">
    </form> -->
    <h1>Student Register</h1>
    <form action="newconn.php" method="POST">
        
        <div class="left-side">
            <input type="text" name="nom" placeholder=" Lastname">
            <input type="text" name="prenom" placeholder=" Firstname">
            <!-- <select name="genre">
                <option value="0">Masculin</option>
                <option value="1">Feminin</option>
                </select>
                -->
            <input type="text" name="genre" placeholder="genre">
            <input type="date" name="naissance" placeholder=" Birthday">
            <input type="text" name="filière" placeholder=" Field">
            <input type="nombre" name="promotion" placeholder="Promotion Name">
            <!-- <input type="date" name="date_enregistrement" placeholder="Today Date"> -->
            <input type="text" name="matricule" placeholder="Matricule">
            <input type="submit" value="Create" class="sub">
        </div>

        <div class="right-side">
            <div class="upload">
                <input type="file" name="uplf">
            </div>
        </div>
        </form>
        
</body>
</html>


