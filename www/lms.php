<?php

header('Content-Type: text/html;');
require_once(dirname(__FILE__).'/lib/TalentLMS.php');

$API_KEY = getenv('TALENT_API_KEY');
$LMS_SECRET = getenv('LMS_SECRET');
$email = $_GET['email'];
$secret = $_GET['secret'];
if ($secret == $LMS_SECRET) {
    try{
        TalentLMS::setApiKey($API_KEY);
        TalentLMS::setDomain('learning.healthlens.org');

        $user = TalentLMS_User::retrieve(array('email' => $email));

        echo "<table class='table table-hover'>";
        foreach ($user['courses'] as $course) {
            $url = TalentLMS_Course::gotoCourse(
                array('user_id' => $user['id'], 'course_id' => $course['id']));
            echo "<tr><td><a href='{$url['goto_url']}' target='_blank'>{$course['name']}</a></td>";
            $percent = $course['completion_percentage'];
            switch($percent)
            {
            case "0":
                echo  "<td><span class='badge new'>New</span></td><td/>";
                break;
            case "100":
                echo "<td><span class='badge complete'>Completed</span></td><td/>";
                break;
            case "100":
            default:
                echo "<td><span class='badge inprogress'>In Progress</span></td><td><div class='progress progress-striped'><div class='progress-bar progress-bar-success' role='progressbar' aria-valuenow='${percent}' aria-valuemin='0' aria-valuemax='100' style='width: ${percent}%;'><span class='sr-only'>${percent}% Complete</span></div></div></td>";
            }
            echo "</tr>";
        }
        echo "</table><h3><a href='${user['login_key']}' target='_blank'>My Course Dashboard</a></h3>";
    }
    catch(Exception $e){
        //echo "var_dump($e);
        echo "There was an error loading your courses.  Please contact Healthlens support.";
        $http_status = $e->getHttpStatus();
        if ($http_status == 404) {
        }
    }
}
?>
