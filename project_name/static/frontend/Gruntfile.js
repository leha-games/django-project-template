module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - <%= grunt.template.today("dd-mm-yyyy") %> */\n'
            },
            dist: {
                files: {
                    '../js/global.min.js': [
                    ]
                }
            }
        },
        stylus: {
            compile: {
                options: {
                    compress: false
                },
                files: {
                    'tmp/global.stylus.css': 'stylus/global.styl'
                }
            }
        },
        csso: {
            dist: {
                files: {
                    '../css/global.min.css': [
                        'tmp/global.stylus.css'
                    ]
                }
            }
        },
        watch: {
            files: ['stylus/*'],
            tasks: ['stylus', 'csso']
        }
    });

    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-csso');

    grunt.registerTask('default', ['uglify', 'stylus', 'csso']);

};
