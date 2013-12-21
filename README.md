cloudspring.lms
===============

This is a Plone product that integrates courses from the [Talent
LMS](http://talentlms.com) as a tile for the
[collective.cover](https://github.com/collective/collective.cover) product. 

![Screenshot](https://raw.github.com/a-pasquale/cloudspring.lms/screenshot.png)

To use this product, you must symlink the files in the www directory (lms.php
and the TalentLMS API files) to the root of your webserver.  Also, set the
environment variables for your Talent LMS API Key and your shared secret.  Here
is an example for Nginx and php-fpm:

location ~ \.php$ {
   ...
   fastcgi_param TALENT_API_KEY "your key";
   fastcgi_param LMS_SECRET "your secret";
}
