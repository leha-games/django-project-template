var gulp = require('gulp'),
    sass = require('gulp-sass'),
    watch = require('gulp-watch'),
    postcss = require('gulp-postcss'),
    sourcemaps = require('gulp-sourcemaps'),
    autoprefixer = require('autoprefixer');

// Static Server + watching scss/html files
gulp.task('serve', ['sass'], function() {
    gulp.watch("**/*.scss", ['sass']);
});

// Compile sass into CSS & auto-inject into browsers
gulp.task('sass', function() {
    return gulp.src("scss/*.scss")
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(postcss([ autoprefixer() ]))
        .pipe(sourcemaps.write('.', {includeContent: false}))
        .pipe(gulp.dest('../css'))
});

gulp.task('default', ['serve']);