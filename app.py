from flask import Flask, render_template, send_file, jsonify, request
from io import BytesIO
import json
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

# CV Data
cv_data = {
    'name': 'Yashwini Shetty',
    'title': 'Senior Automation Test Engineer',
    'subtitle': 'Automation QA Engineer | 8+ Years Experience',
    'contact': {
        'phone': '+966 548045247',
        'email': 'yashwini.j.shetty@gmail.com',
        'linkedin': 'www.linkedin.com/in/yashwini-j-shetty-83b3b7115',
        'location': 'Al Qadisiayah, Riyadh, KSA'
    },
    'profile': '''Highly skilled Automation QA Engineer with 8+ years of experience in mobile and web application testing. 
    Expertise in designing, developing, and executing robust automation test scripts to ensure high-quality software delivery. 
    Experienced in leading QA teams, mentoring testers, and driving process improvements to enhance efficiency and coverage. 
    Proficient in multiple testing frameworks, CI/CD pipelines, and database testing. Strong collaborator with cross-functional teams, 
    passionate about delivering high-quality software and impactful results in fast-paced, dynamic environments.''',
    'summary': '''With 8+ years in Automation and Manual Testing, I specialize in Web & Mobile Applications and APIs, including native, 
    hybrid, cross-platform, and web apps, with Strong skills in Manual Testing. Proficient in Java, Python and currently working with 
    Groovy in Katalon. Experienced with Selenium, Appium, TestNG, Robot Framework, TestRigor, SmartBear ReadyAPI, and REST API and katalon.
    
    Skilled in Test Planning, Design, Execution, and Defect Reporting using JIRA, ClickUp and Redmine. Leading testing of complex modules 
    like Benefit and Contribution Management, ensuring functional accuracy, regulatory compliance, and seamless integration with other systems.
    
    Driving QA process improvements by aligning test cases with developer commits, establishing automation checkpoints, and enhancing overall 
    test coverage. Proficient in automation (Java,TestNG,WebDriver), SQL, and CI/CD pipelines (CircleCI,GitHubActions,Jenkins). 
    Leading and mentoring QA teams, training manual testers and interns, and collaborating closely with BAs and Product Owners to refine 
    requirements and acceptance criteria. Strong communicator, proactive in Agile environments, and committed to delivering high-quality 
    software efficiently.''',
    'education': [
        {
            'degree': 'Master of Engineering',
            'institution': 'Manipal University - MS Visvesvaraya Technological University',
            'period': '2016 - 2018',
            'description': 'Specialized in Engineering with focus on advanced technical subjects'
        },
        {
            'degree': 'Bachelor of Engineering',
            'institution': 'Visvesvaraya Technological University',
            'period': '2012 - 2016',
            'description': 'Foundation in Engineering principles and practices'
        }
    ],
    'skills': {
        'Programming Languages': ['Java', 'Groovy', 'Python', 'SQL', 'Gherkin'],
        'Testing Frameworks': ['Selenium', 'Appium', 'TestNG', 'Cucumber', 'Robot Framework', 'TestRigor'],
        'Automation Tools': ['Katalon Studio', 'SmartBear ReadyAPI', 'REST API', 'Maven', 'Docker'],
        'CI/CD Tools': ['Jenkins', 'Circle CI', 'GitHub Actions', 'GitLab CI'],
        'Project Management': ['Jira', 'ClickUp', 'Redmine', 'Agile/Scrum'],
        'Version Control': ['GitHub', 'GitLab', 'Git'],
        'Testing Types': ['Web Testing', 'Mobile Testing (Native, Hybrid, Cross-platform)', 'API Testing', 'Database Testing'],
        'Mobile Tools': ['Android Studio', 'Xcode', 'Flutter Inspector', 'BrowserStack'],
        'Operating Systems': ['Windows', 'Mac', 'Linux'],
        'Other': ['Test Planning', 'Test Design', 'Defect Reporting', 'Team Leadership', 'Mentoring']
    },
    'experience': [
        {
            'title': 'Senior Automation Test Engineer',
            'company': 'Current Organization',
            'location': 'Riyadh, KSA',
            'period': 'Present',
            'responsibilities': [
                'Leading testing of complex modules like Benefit and Contribution Management systems',
                'Ensuring functional accuracy, regulatory compliance, and seamless system integration',
                'Driving QA process improvements by aligning test cases with developer commits',
                'Establishing automation checkpoints and enhancing overall test coverage',
                'Leading and mentoring QA teams, training manual testers and interns',
                'Collaborating with Business Analysts and Product Owners to refine requirements',
                'Managing test execution using Katalon Studio with Groovy',
                'Implementing CI/CD pipelines with CircleCI, GitHub Actions, and Jenkins'
            ]
        },
        {
            'title': 'Automation QA Engineer',
            'company': 'Previous Experience',
            'location': 'Various',
            'period': '8+ Years Total Experience',
            'responsibilities': [
                'Designed and developed robust automation test scripts for web and mobile applications',
                'Performed comprehensive testing of native, hybrid, and cross-platform applications',
                'Executed API testing using REST API and SmartBear ReadyAPI',
                'Conducted database testing and validation using SQL',
                'Implemented test automation frameworks using Selenium, Appium, and TestNG',
                'Managed defect tracking and reporting using JIRA, ClickUp, and Redmine',
                'Collaborated with cross-functional teams in Agile environments',
                'Utilized BrowserStack for cross-browser and cross-device testing'
            ]
        }
    ],
    'highlights': [
        {
            'icon': '🎯',
            'title': '8+ Years',
            'subtitle': 'Experience in QA'
        },
        {
            'icon': '🤖',
            'title': 'Automation Expert',
            'subtitle': 'Multiple Frameworks'
        },
        {
            'icon': '👥',
            'title': 'Team Leadership',
            'subtitle': 'Mentoring & Training'
        },
        {
            'icon': '🌍',
            'title': 'IQAMA Holder',
            'subtitle': 'Working in KSA'
        }
    ],
    'certifications': [
        'Agile & Scrum Methodologies',
        'Test Automation Frameworks',
        'CI/CD Pipeline Implementation'
    ]
}

@app.route('/')
def home():
    return render_template('index.html', cv=cv_data)

@app.route('/api/cv')
def api_cv():
    """API endpoint to get CV data in JSON format"""
    return jsonify(cv_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
