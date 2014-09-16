var os = require("os");
var pkg = require("./package.json");

'use strict';

module.exports = function(grunt) {

    grunt.initConfig({
        package: pkg,
        gitcheckout: {
            task: {
                options: {
                    branch: os.platform() == "win32" ? "win32" : "master"
                }
            }
        },
        publish: {
            task: {
                options: {
                    registry: pkg.publishConfig.registry
                },
                src: [ "." ]
            }
        },
        shell: {
            task: {
                // uncheckout the package.json
                command: "git checkout -- package.json"
            }
        }
    });

    grunt.loadNpmTasks('grunt-git');
    grunt.loadNpmTasks('grunt-npm-install');
    grunt.loadNpmTasks('grunt-publish');

    grunt.registerTask('writePackageJson', 'Set the platform in the package.json', function() {
        pkg.name += "-" + os.platform();
        grunt.file.write("./package.json", JSON.stringify(pkg, null, 4));
    });

    grunt.registerTask('default', 'Default Task', function() {
        var tasks = ['gitcheckout:task', 'writePackageJson', 'npm-install', 'publish:task', 'shell:task'];
        grunt.task.run(tasks);
    });
};
