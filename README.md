# PP4 Full-Stack Toolkit: Blogster

![Blogster](https://github.com/Humanslaughter/pp4-blog/assets/122393963/fd86cacc-05c9-4dc4-a5ef-fe7861be38da)

This is a blog website that I made with the help of the walkthrough project "I Think Therefore I Blog" by Code Institute.
On the main/home page is where you can see the list of posts made by the website's bloggers, with a title, excerpt, image, who's the blogger, and when it was uploaded.

As a site-dedicated blogger, you can add, edit, and delete posts from the UI, they also have staff status for the ability to view, add, edit, and delete posts from the Admin panel.

As a site user, you can click on the post you want to read, if the user has signed up for an account and is logged in, they can also leave comments on each post.
The Admin has to approve the comments before they show up on the page. You can edit and delete a comment when it has been approved or while it's pending on being approved.

On the About page, you can read about the site owner/creator and fill out a form if you're interested in contacting them or maybe becoming a blogger for the site.

When a user is logged in, they're username will be shown as "Logged in as" at the upper right corner of the page, if you're not logged in or don't have an account it will say "Not logged in".

[Visit Blogster](https://pp4-blog-app-c04802231ec3.herokuapp.com/)

---

## Contents

* [User Experience (UX)](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Color Scheme](#color-scheme)
  * [Typography](#typography)

* [Features](#features)
  * [Navigation Bar](#navigation-bar)
  * [Footer](#footer)
  * [About](#about)
  * [Register](#register)
  * [Login/Logout](#login-logout)
  * [Logged In As/Not Logged In](#logged-in-as-not-logged-in)
  * [Post List](#post-list)
  * [Post Detailed View](#post-detailed-view)
  * [Add Post](#add-post)
  * [Edit/Delete Posts](#edit-delete-posts)
  * [Comments Logged In/Not Logged In](#comments-logged-in-not-logged-in)
  * [Comment Awaiting Approval](#comment-awaiting-approval)
  * [Edit/Delete Comments](#edit-delete-comments)

*[Future Features](#future-features)

*[Technologies Used](#technologies-used)
  *[Languages](#languages)
  *[Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Testing](#testing)
  * [Validator Testing](#validator-testing)
  * [Futher Testing](#futher-testing)
  * [Known Bugs & Issues](#known-bugs--issues)

*[Deployment & Local Development](#deployment--local-development)
 	* [Local Development](#local-development)
  		* [How To Fork](#how-to-fork)
  		* [How To Clone](#how-to-clone)

* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

---

## User Experience (UX)

### User Stories

* User Story: Post List Pagination #1<br>
  As a User I can view a paginated list with posts so that I can pick the post I want to read
    
  Acceptance Criteria
  - Have a paginated list of posts accessible to the user from the homepage or dedicated blog page.
    
  Tasks
  - [x] Implement Pagination Logic.
  - [x] Create UI for Paginated List.
  - [x] Integrate Frontend with Pagination Logic.
  - [x] Display Paginated List on Homepage/Dedicated Blog Page.
  - [x] Test Pagination Functionality. 

* User Story: Read post #2<br>
  As a **User** I can **click a post** so that **I can read the text fully**

  Acceptance Criteria
  - A detailed view of a post can be seen when a post title is clicked.

  Tasks
  - [x] - Design Post Detail Page.
  - [x] - Implement Frontend Click Functionality.
  - [x] - Fetch and Display Post Content.
  - [x] - Test Click-to-Read Functionality.

* User Story: Read Comments #3<br>
  As a User/Admin I can view comments on a post so that I can read user's conversations

  Acceptance Criteria
  - Admin can view one or more comments from users.
  - A user can click the comment thread to read all the conversations.

  Tasks
  - [x] - Design Comment Display.
  - [x] - Implement Backend for Comment Retrieval.
  - [x] - Integrate Comment Display in Post View.
  - [x] - Test Comment Viewing Functionality.

* User Story: Account Registration #4<br>
  As a **User** I can **register an account** so that **I can leave comments on posts**

  Acceptance Criteria
  - A user can register an account.
  - Then the user can log in.
  - When the user is logged in they can comment on posts.

  Tasks
  - [x] Design and implement the Registration Form.
  - [x] Implement Sign Up, Sign In, and Sign Out functionality.
  - [x] Implement Commenting for logged in users.
  - [x] Test functionality.

* User Story: Comment On Posts #5<br>
  As a **User** I can **comment on a post** so that **I can share my thoughts.**

  Acceptance Criteria
  - Logged-in users can submit comments on posts.

  Tasks
  - [x] Design Comment Section.
  - [x] Implement Comment Submission Backend.
  - [x] Integrate Comment Section Frontend.
  - [x] Display Comments on Posts.
  - [x] Test Functionality.

* User Story: Edit Or Delete Comments #6<br>
  As a **User** I can **edit or delete my comments on posts** so that **I can join in on the conversation**

  Acceptance Criteria
  - A logged-in user can edit their comment.
  - A logged-in user can delete their comment.

  Tasks
  - [x] Design Edit Comment Interface.
  - [x] Implement Edit Comment Backend.
  - [x] Design Delete Comment Confirmation.
  - [x] Implement Delete Comment Backend.
  - [x] Integrate Comment Editing and Deletion Frontend.
  - [x] Test Edit and Delete Functionality.

* User Story: Create Posts #7<br>
  As a **Admin** I can **create posts** so that **I can share content with site users**

  Acceptance Criteria
  - A logged-in user can create blog posts.

  Tasks
  - [x] Design Post Creation Form.
  - [x] Implement Post Creation Backend.
  - [x] Integrate Post Creation Frontend.
  - [x] Test functionality.

* User Story: Draft Post #8<br>
  As a **Admin** I can **save my post as a draft** so that **I can continue/finish writing my post later**

  Acceptance Criteria
  - A logged-in user can save a blog post as a draft.
  - They can then continue/finish writing the post at another time.

  Tasks
  - [x] Implement "Draft" Field.
  - [x] Create Draft Storage in Backend.
  - [x] Enable Draft Retrieval.
  - [x] Test Draft functionality.

* User Story: Comment Approval #9<br>
  As a **Admin** I can **approve or disapprove a comment** so that **I can manage and remove unpleasant comments**

  Acceptance Criteria
  - A logged-in user can approve comments.
  - A logged-in user can disapprove comments.

  Tasks
  - [x] Implement Approve Field.
  - [x] Implement Backend Logic for Comment Approval.
  - [x] Integrate Approval Functionality into Frontend.
  - [x] Test Comment Approval functionality.

* User Story: About Page #10<br>
  As a **User** I can **click the About link** so that **I can read about the blog**

  Acceptance Criteria
  - A visible About text will show when the About link is clicked.

  As a **Admin** I can **create or update content on the About page** so that **users can read about my blog**

  Acceptance Criteria
  - The About Page is visible in the admin panel.

   Tasks
  - [x] Create About Page App.
  - [x] Integrate About Link in User Interface.
  - [x] Implement About Page Display.
  - [x] Design Admin Panel Section for About Page.
  - [x] Integrate Admin Panel Link for About Page.
  - [x] Implement Content Creation/Update Functionality.
  - [x] Verify About Page Visibility in Admin Panel.
  - [x] Test About Link and Page Display.
  - [x] Test Admin Content Creation and Update.

* User Story: Edit Posts #17<br>
  As a **Admin** I can **edit posts** so that **I can correct any mistakes or update content.**

  Acceptance Criteria
  - A logged-in user can edit blog posts.

  Tasks
  - [x] Design Edit Post Interface.
  - [x] Implement Edit Post Backend.
  - [x] Integrate Edit Post Frontend.
  - [x] Test Edit Functionality.

* User Story: Delete Posts #18<br>
  As a **Admin** I can **delete posts** so that **I can remove any post I don't like**

  Acceptance Criteria
  - A logged-in user can delete blog posts.

  Tasks
  - [x] Design Delete Post Confirmation.
  - [x] Implement Post Deletion Backend.
  - [x] Integrate Post Deletion Frontend.
  - [x] Test Post Deletion Functionality.

* User Story: Contact Form #19<br>
  As a **Potential Collaborator** I can **fill out a contact form** so that **I can request a user for collaboration**

  Acceptance Criteria
  - Contact Form Access on About page.
  - Form Fields.
  - Submit Button.

  Tasks
  - [x] - Design and implement Contact Form.
  - [x] - Implement Contact Form Backend.
  - [x] - Integrate Frontend with Contact Form Logic.
  - [x] - Test Contact Form Functionality.

* User Story: Store Contact Requests #20<br>
  As a **Site Owner** I can **store contact requests in the database** so that **I can review them**

  Acceptance Criteria
  - A form is available for users to submit contact requests on the About page.
  - Submitted contact requests are in the database.
  - Site owner can access and review stored contact requests.

  Tasks
  - [x] - Implement Backend for Storage.
  - [x] - Integrate Frontend with Form and Backend.
  - [x] - Create Database Schema for Requests.
  - [x] - Implement Access for Site Owner.
  - [x] - Test Functionality.

* User Story: Mark Collaboration Requests As Read #21<br>
  As a **Site Owner** I can **mark collaboration requests as "read"** so that **I can see how many I still need to process**

  Acceptance Criteria
  - A "Read" Field is available for collaboration requests.
  - Clicking "Read" updates the request status to "read".

  Tasks
  - [x] - Implement "Read" Field.
  - [x] - Update Request Status in the Database.
  - [x] - Test "Read" Field Functionality.
  - [x] - Ensure Accessibility and Usability.

## Design

### Colour Scheme
![pp4 color scheme](https://github.com/Humanslaughter/pp4-blog/assets/122393963/8ef1d59b-c308-4e8b-b783-8bf20d7db2f0)

### Typography
Font Family Roboto
Font Family Lato

## Features

### Navigation Bar
![NavBar](https://github.com/Humanslaughter/pp4-blog/assets/122393963/b08bce89-b2d7-410e-802e-f27fc7cedc65)

### Footer
![Footer](https://github.com/Humanslaughter/pp4-blog/assets/122393963/9960bfef-4494-4947-a418-da6e56523fe5)

### About
![About 2](https://github.com/Humanslaughter/pp4-blog/assets/122393963/057a495c-6f45-454e-b4c8-7d24c30f951e)

### Register
![Register](https://github.com/Humanslaughter/pp4-blog/assets/122393963/9c8a1d92-420b-4ae9-98b6-6e6cf78be50b)

### Login/Logout
![Login](https://github.com/Humanslaughter/pp4-blog/assets/122393963/591eeb97-9aac-45b2-a02e-702727a5be4b)<br>
![Logout](https://github.com/Humanslaughter/pp4-blog/assets/122393963/fdf6f191-cb52-42ae-a032-7018e7624080)

### Logged In As/Not Logged In
![Logged in](https://github.com/Humanslaughter/pp4-blog/assets/122393963/d2034a08-3dea-42ee-964f-bfa58922c150)<br>
![Not logged in](https://github.com/Humanslaughter/pp4-blog/assets/122393963/bb706809-7c6a-4ca6-8e0a-5843b97ff7ab)

### Post List
![Post List](https://github.com/Humanslaughter/pp4-blog/assets/122393963/faf6491d-64dd-4e7b-863e-0c0d243bb9e5)

### Post Detailed View
![Post detailed view](https://github.com/Humanslaughter/pp4-blog/assets/122393963/356bd629-e8ea-47c5-9ceb-5de7a3cd73c9)

### Add Post
![Add post](https://github.com/Humanslaughter/pp4-blog/assets/122393963/0c86daf6-3d08-422a-a764-1bb0e7796cfd)

### Edit/Delete Posts
![Edit delete post 1](https://github.com/Humanslaughter/pp4-blog/assets/122393963/dd9e1ebd-1dfe-4134-a78d-bab3a997ea79)<br>
![Edit delete post 2](https://github.com/Humanslaughter/pp4-blog/assets/122393963/3152ea1e-c52f-4f1b-95e8-afe4bebd11f9)<br>
![Update post](https://github.com/Humanslaughter/pp4-blog/assets/122393963/3d55bdb3-fdf8-4c2b-9eae-d73ba053104a)<br>
![Delete post](https://github.com/Humanslaughter/pp4-blog/assets/122393963/dd848955-39ac-43c9-b535-5d382ea8abf5)

### Comments Logged In/Not Logged In
![Comments logged in](https://github.com/Humanslaughter/pp4-blog/assets/122393963/35e3cbfa-53bd-44d7-a3cd-1168be26d2a7)<br>
![Comments logged out](https://github.com/Humanslaughter/pp4-blog/assets/122393963/9413f1da-0206-4fb9-a10c-c3995951133f)

### Comment Awaiting Approval
![Comment awaiting approval](https://github.com/Humanslaughter/pp4-blog/assets/122393963/072bf84f-aa8e-4645-a62d-aa5ae90fc860)

### Edit/Delete Comments
![Update comment](https://github.com/Humanslaughter/pp4-blog/assets/122393963/2dc12664-e9b3-43f7-acf8-c403c1465f18)<br>
![Delete comment](https://github.com/Humanslaughter/pp4-blog/assets/122393963/2a96c387-ed4a-4558-a32e-0ca9b25c326a)<br>
![Update comment not approved](https://github.com/Humanslaughter/pp4-blog/assets/122393963/60c857c0-24cd-43c8-8494-dcc2b83d840d)


## Future Features
- Authentication via social media.
- Enable email verification and 2-step authintication for more account security.
- User profiles, users can add/edit/delete their own posts.
- Share posts to other social media platforms.
- Ability to send private messages to other users.

## Technologies Used

### Languages

- HTML.
- CSS.
- Python.

### Frameworks, Libraries & Programs Used

- Bootstrap 5.
- Crispy Bootstrap 5.
- Google Fonts.
- Font Awesome.
- Git.
- GitHub.
- Django.
- Django AllAuth.
- Summernote.
- Django Staticfiles.
- Ckeditor.
- Crispy Forms.
- Cloudinary.
- Cloudinary Storage.
- Heroku.
- ElephantSQL.
- Whitenoise.
- Gunicorn.
- Django JS Asset.

## Testing

### Validator Testing
 - W3C - Passed.
 - CI Python Linter - All clear.

### Futher Testing
- Testing was done throughout the development, with multiple deployments in between to make sure the site's layout/design, forms, views, url's, functions, and requests responds the way it should.
- A large amount of testing was done to ensure that everything were linking correctly.
- The site has been viewed and tested on both desktop and mobile.
- Links to add, edit, and delete posts and comments work as intended and only shows up for users that is autherized and has permission. Auth for register, login, and logout work as intended as well.
- Contact form on About page sends a rewuest with the name, email, and message in it to the admin panel. If fields are empty an error occurs telling those fields can't be empty.
- Clicking on a post link works as intended.
- Add post page works as indended.

### Known Bugs & Issues
- The slug field in Add Post doesn't automatically fill when a user with staff/posting permission is writing the title, so the post_slug field has to be visible in the Add Post view so it can be written manually. I haven't been able to figure it out as for now with slugify/auto populate, but it's something I'm planning on fixing in the future. 

## Deployment & Local Development

### Local Deployment

Deployed using Heroku.

1. Log in/sign up to Heroku.
2. Go to your Heroku App and click on "Deploy".
3. At section "Deployment method", click "GitHub" and connect your account with Heroku.
4. When you're connected, search for the project you wanna connect the app to and click on it.
5. Click "Deploy Branch".
6. Your app will now be deployed to GitHub and when it's done you can click "Open App".

#### How to Fork
Fork the repository:<br>
	1. Log in/sign up to GitHub.
 	2. Go to the repository for this project [pp4-blog](https://github.com/Humanslaughter/pp4-blog).
	3. Click the 'Fork' button in the top right corner.

#### How to Clone
Clone the repository:<br>
	1. Log in/sign up to GitHub.
 	2. Go to the repository for this project [pp4-blog](https://github.com/Humanslaughter/pp4-blog).
	3. Click the code button, select which one you want to clone with (HTTPS, SSH or GitHub CLI) and copy the link shown.
 	4. Open the terminal in a code editor and change the current working directory to a location of your choice to use for the cloned directory.
	5. Type 'git clone' in the terminal, paste the link that you copied in step 3 and then press enter.

## Credits

### Code

- I was coding along the Code Institute walkthrough project "I Think Therefore I Blog". All blog posts comes from their fixtures posts that I added images to from Google.

### Content

Code Institute's module for Portfolio Project 4: "Full-Stack Toolkit"
  - User Story Issues.
  - User Story Template.

###  Media

- [Placeholder image](https://pixabay.com/photos/wordpress-blogging-writing-typing-923188/)

Blog post images:
[Image](https://unsplash.com/photos/silhouette-of-woman-raising-her-right-hand-IevaZPwq0mw)
[Image]([Image](https://javaconceptoftheday.com/history-of-programming-languages/))
[Image](https://medium.com/swlh/introduction-to-javascript-basics-cf901c05ca47)
Imagehttps://www.udemy.com/course/the-ultimate-beginners-guide-to-django-django-2-python-web-dev-website/
https://www.activestate.com/blog/top-10-coding-mistakes-in-python-how-to-avoid-them/
https://jaydevs.com/why-soft-skills-matter-when-hiring-a-software-developer/
https://unsplash.com/photos/person-writing-on-white-paper-gcsNOsPEXfs
https://www.hostinger.com/tutorials/web-developer-portfolio
https://medium.com/@sanjay.mohindroo66/scrum-the-agile-framework-transforming-project-management-bb66f4487d28
https://www.marceldigital.com/blog/what-is-agile-web-development-everything-you-need-to-know
https://medium.com/javarevisited/from-spaghetti-code-to-clean-code-a-step-by-step-guide-to-refactoring-in-java-7352d7ddf28a
varevisited/from-spaghetti-code-to-clean-code-a-step-by-step-guide-to-refactoring-in-java-7352d7ddf28a
https://www.linkedin.com/pulse/how-pick-your-first-programming-language-different-ways-alam-gilani
https://builtin.com/software-engineering-perspectives/google-fu

###  Acknowledgments

- Student Care, CI.
