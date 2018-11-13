if __name__ == "__main__":
    message = "!zsuetaM yadhtriB yppaH" [::-1]
    print(message)


var startTime = new Date().getTime();
var interval = setInterval(function()){
    if(new Date().getTime() - startTime > 86400000){
        clearInterval(interval);
        return;
      }
    console.log("Happy Birthday Mateusz!");

}, 1000);

#birthday::before{
content: "Happy";
}