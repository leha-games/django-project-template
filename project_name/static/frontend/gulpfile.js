var gulp = require('gulp'),
    stylus = require('gulp-stylus'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat');

var paths = {
    scripts: [
        './bower_components/jquery/dist/jquery.min.js',
        './scripts/app.js'
    ],
    stylus: 'stylus/**'
};

gulp.task('js', function() {
    gulp.src(paths.scripts)
        .pipe(uglify())
        .pipe(concat('global.min.js'))
        .pipe(gulp.dest('../js'))
});

gulp.task('stylus', function () {
  gulp.src('./stylus/global.styl')
    .pipe(stylus())
    .pipe(gulp.dest('../css'))
});

gulp.task('watch', function() {
    gulp.watch(paths.scripts, ['js']);
    gulp.watch(paths.stylus, ['stylus']);
});

gulp.task('default', ['stylus', 'js']);
