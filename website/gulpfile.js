// The require statement tells Node to look into the node_modules folder for a package named gulp. 
// Once the package is found, we assign its contents to the variable gulp.

var gulp = require('gulp');
gulp.task('hello', function() {
  console.log('Hello Zell');
});
