var gulp = require('gulp'),
    sass = require('gulp-sass'),
    watch = require('gulp-watch'),
    postcss = require('gulp-postcss'),
    sourcemaps = require('gulp-sourcemaps'),
    autoprefixer = require('autoprefixer');

var paths = {
    styles: {
        src: 'scss/*.scss',
        dest: '../css'
    }
};

function styles() {
    return gulp
        .src(paths.styles.src)
        .pipe(sourcemaps.init())
        .pipe(sass())
        .pipe(postcss([ autoprefixer() ]))
        .pipe(sourcemaps.write('.', {includeContent: false}))
        .pipe(gulp.dest(paths.styles.dest))
}

var serve = gulp.series(styles, function() {
    gulp.watch("**/*.scss", styles);
})

gulp.task('default', serve);