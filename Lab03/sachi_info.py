
#This File will contain the information to be displayed in your portfolio

#CHANGE BELOW
profile_picture = "Images/profile.JPG"
about_me = "My name is Sachi Goel, and I'm from Seattle, WA. I am currently studying Computer Science at the Georgia Institute of Technology, with concentrations in Intelligence and Modeling & Simulation. I am passionate about exploring the intersection of computer science within all discipline of thought, namely Business and Finance. "


#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/sachigoel/"
my_github_url = "https://github.com/computer-s-2"
my_email_address = "sachigoel27@gmail.com"


education_data ={
    'Degree': 'Bachelor of Science in Computer Science',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': '2028',
    'GPA': '4.0'
}
course_data = {
    "code":["CS 1301", "CS 2050", "MATH 1554", "PHYS 2211", "CS 1100"], 
    "names":["Intro to CS", "Discrete Mathematics", "Linear Algebra", "Mechincal Physics", "CS Seminar"], 
    "semester_taken":["1st", "1st", "1st", "1st", "1st"],
    "skills":["Learned the funadmanetals of Python and Web Devolpment through HTML & CSS and JavaScript", "Learned the logic behind machine learning algorthims", "Gained a deep understanding of the background math of computer systems and algorithms like search engine ranking and data compressions through SVD","Vector based understanding of mechincal physics properties", "Computer Science job preperation"],
    }
experience_data = {
    "Research Assistant of Machine Learning for Finance Markets Research Group": (["- Worked at Georgia Tech's trading floor with a 20 person research team",
                                                                          "- Employed regularized regression, tree-based methods, neural networks, and deep learning to predict the causal effect of a policy or regulatory change within quantitative trading, investment, corporate finance, FinTech, and banking"],"Images/stock.jpg"),
    "UI/UX Intern at M.K. Bolling Insurance Agency":(["- Utilized data analytics to identify weaknesses in the past website and developed a custom full-stack website with HTML, CSS, and JavaScript, enhancing their online presence and integrating insurance calculation and communication software",
                                                           "- Assisted in 10+ Spanish insurance calls, improving client communication", "- Designed logo to strengthen brand identity; leveraged community as an athlete to advertise their company during 15 local football games"],"Images/logo.mk.png"),
    "Gymnastics Coach at Plano Parks and Recreation":(["- Conducted rigorous evaluations and assessments for over 100 athletes during camps and practices; implemented tailored development plans that improved individual performance levels and athlete safety, contributing to overall program success", "- Provided instruction in Spanish, fostering inclusivity"],"Images/plano.logo.png"),
    "Private Online Tutor at SummTutoring": (["- Organized and implemented 100+ lesson plans for elementary, middle, and high school math, reading, and science", "- Assessed class assignments, determined grades, and reviewed work with struggling 10+ students to bolster individual success"], "Images/summ.webp"),
    "Business Owner of ByCrochetCorner":(["- Sold handmade, sustainably sourced, and produced crochet items", "- Consistently doubled sales each year through improved customer service, SEO optimization, ad development, and increased online presence on the company's Instagram"], "Images/crochet.jpg")

}

projects_data = {
    "AI ATL Hackathon: Engel Score Predictor using NER, RAG, and LLM Models": ["- Worked with a team to automate Engel score predictions (classifies efficacy of epileptic treatments) by taking a synthetic data set and finding NER with the Anthropic API, which was then put through NEO4J to extract relationships between symptoms","- Created a RAG algorithm to query the knowledge graph, which was parsed through a fine-tuned Gemini model to output the Engel score and the reason for how the model arrived at that conclusion"],
    "Winner of University of Washington at Bothell AI Hackathon: Freakquency": ["- Created a visualization of the app “Freakquency,” which given a patient’s medical history and current lifestyle habits, predicts the user's likelihood of developing certain lifestyle diseases and creates a daily and monthly action plan", "- Won 1st in the biotechnology track against 20 teams and placed 3rd overall amongst 92 projects with 358 participants", "- Secured recognition for developing a groundbreaking healthcare service solution that generated 200+ positive feedback responses; leveraged this success to gain an invitation to the competitive Avanade hackathon"],
    "Fake News Detector with Convolutional Neural Network": ["- Created a CNN model that automatically detects fake and real news articles with the Keras TextVectorization layer", "- Trained the model with the ISOT Fake News Dataset, yielding a 98.74% accuracy rate on categorizing news articles"]
}

programming_data = {
    "Python": 90,
    "HTML & CSS": 80,
    "JavaScript": 60,
    "PHP": 40,
    "Java": 30
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    # "Python": "🐍",
    # "Java": "☕",
    # "C": "🔍",
}
spoken_icons = {
    # "French": "🇫🇷",
    # "English": "🇬🇧",
    # "Spanish":"🇪🇸"
}

#CHANGE BELOW
spoken_data = {
    "English": "Fluent",
    "Spanish": "Working Proficiency",
    "Hindi": "Native",
}
leadership_data = {
    "President of Artificial Intelligence Club": (["- Educated club members on theory and Python syntax to develop a comprehensive understanding of AI algorithms", "- Overhauled and synthesized past teaching material to better appeal to high school students", "- Increased club membership by 700%"],"Images/ai.jpg"),
    "Competition Director of Computer Science Honors Society (CSHS)": (["- Collaborated with CS Council and CSHS teachers to organize lesson plans and create material to teach different coding skills (HTML & CSS, bootstrap, JQuery, SQL, Python, etc), teaching 50+ students", "- Spearheaded the competition branch and created material to teach Python and competitive coding concept", "- Executed mock school coding competitions and organized competitions with other schools"], "Images/cshs.jpeg"),
    "President of Competitive Coding Club": (["- Organized learning materials in Java and Python teaching members theory, syntax, and practice questions every week", "- Coached 60+ club members on the worldwide competition, Lockheed Martin, making it to the semi-finals"], "Images/coding.jpeg")

}
activity_data={
    "Member of High-Performance Computing Club": ["- Participated in a GPU programming workshop, learning CUDA and accelerating computations by up to 10x using parallel processing on Georgia Tech’s PACE supercomputing cluster"],
    "Fellow of Girls In Venture Capital": ["- Selected as one of 15 out of 100 women in the inaugural cohort, focusing on leveraging technology to drive investment decisions and enhance startup ecosystems, using data-driven approaches to assess product-market fit and potential scalability"]
}
