var incrementalAngle = 0.0;

function setup(){
  var canvas = createCanvas(windowWidth, windowHeight);
  canvas.parent('bubbly');
  smooth();
  background(0);

  ellipse(windowWidth/2, windowHeight/2, 200, 200);
  drawCircles(30, 200);
}

function draw(){

}

var drawCircles=function (circlesNumber,bigCircleNumber){
  var angle = incrementalAngle;

  for(i = 0; i < circlesNumber; i++){
    ellipse(bigCircleNumber * cos(incrementalAngle)+ windowWidth/2 , bigCircleNumber * sin(incrementalAngle) + windowHeight/2, circlesNumber, circlesNumber);
    incrementalAngle += TWO_PI / circlesNumber;  
  } 
}