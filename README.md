# Personal Playlist

**CS178: Cloud and Database Systems — Project #1**
**Author:** Noelle Burke
**GitHub:** noelleburke-dotcom

---

## Overview
This project is for music lovers! In this app you can keep track of your favorite songs. Add or delete songs from the playlist. Multiple users can use this site!

---

## Technologies Used

- **Flask** — Python web framework
- **AWS EC2** — hosts the running Flask application
- **AWS RDS (MySQL)** — relational database for [describe what you stored]
- **GitHub Actions** — auto-deploys code from GitHub to EC2 on push

---

## Project Structure

```
ProjectOne/
├── flaskapp.py          # Main Flask application — routes and app logic
├── dbCode.py            # Database helper functions (MySQL connection + queries)
├── creds.py   
├── ProjectOneSchema.sql  
├── static/   
│   ├── add_user.css
│   ├── delete_user.css
│   ├── display_user.css
│   ├── home.css
│   ├── update_playlist.css
│   ├── update_users.css
│   ├── update_playlist.css
│   ├── user_playlist.css  
├── templates/
│   ├── home.html       # landing page
│   ├── add_user.html
│   ├── delete_user.html
│   ├── display_user.html
│   ├── update_playlist.html
│   ├── update_user.html         
│   ├── user_playlist.html     
├── .gitignore           # Excludes creds.py and other sensitive files
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/noelleburke-dotcom/cs178-flask-app.git
   cd your-repo-name
   ```

2. Install dependencies:

   ```bash
   pip3 install flask pymysql boto3
   ```

3. Set up your credentials (see Credential Setup below)

4. Run the app:

   ```bash
   python3 flaskapp.py
   ```

5. Open your browser and go to `http://127.0.0.1:8080`

---

## How to Access in the Cloud

The app is deployed on an AWS EC2 instance. To view the live version:

```
http://ec2-13-220-255-157.compute-1.amazonaws.com:8080
```

_(Note: the EC2 instance may not be running after project submission.)_

---

## Credential Setup

This project requires a `creds.py` file that is **not included in this repository** for security reasons.

Create a file called `creds.py` in the project root with the following format (see `creds_sample.py` for reference):

```python
# creds.py — do not commit this file
host = "your-rds-endpoint"
user = "admin"
password = "your-password"
db = "your-database-name"
```

---

## Database Design

### SQL (MySQL on RDS)
+-----------------------------+
| Tables_in_project1-database |
+-----------------------------+
| Artist                      |
| Playlist                    |
| PlaylistSong                |
| Song                        |
| User                        |
+-----------------------------+
Artist holds the list of artists in the playlist. Playlist holds the songs and the information in them like artist duration and whose playlist it is in. PlaylistSong has the all songs in order of when they were added. Songs holds the artist, duration, and the title. User
<!-- Briefly describe your relational database schema. What tables do you have? What are the key relationships? -->

**Example:**

- `[TableName]` — stores [description]; primary key is `[key]`
- `[TableName]` — stores [description]; foreign key links to `[other table]`

The JOIN query used in this project: <!-- describe it in plain English -->

I did not use a DynamoDB table. The data was stored in the RDS tables.

## CRUD Operations

| Operation | Route      | Description    |
| --------- | ---------- | -------------- |
| Create    | `/[route]` | [what it does] |
| Read      | `/[route]` | [what it does] |
| Update    | `/[route]` | [what it does] |
| Delete    | `/[route]` | [what it does] |

---

## Challenges and Insights

<!-- What was the hardest part? What did you learn? Any interesting design decisions? -->
The hardest part was making sure the links went to the correct site. Update user.html often took the user to the user playlist not the update playlist site. I learned to be very specific with what I name the routes. 
On the user playlist I wanted to show stats of the playlist. However, due to the deadline and still having a few bugs, I had to skip those features. 
I had lots of fun with designing the sites! Choosing the colors was so fun! If I had more time I could have added those features and maybe added more to the layouts.
---

## AI Assistance

<!-- List any AI tools you used (e.g., ChatGPT) and briefly describe what you used them for. Per course policy, AI use is allowed but must be cited in code comments and noted here. -->
The ai use was for asking if it was possible to do some things. Making the schema and rds was a large part. Using ai to make the sql fit the schema was a part. Making the sql fit the schema was confusing. Style was a big one. Despite my own code being written and mostly correct, things wouldn't work. I put the code in to ai to check it. Most of the time it was Bootstrap overriding the css file. Lastly I had a huge issue with a route. The update route would take you to the wrong site. I asked over and over how to fix it. I was stumped by the error. 
https://chatgpt.com/c/69cbfb6d-7adc-8328-8b73-979dfc665d34 this conversation was a how to on setting up my database
https://chatgpt.com/c/69cc0a16-c9fc-8330-b266-8df707dd8afd used to troubleshoot and style the app
https://chatgpt.com/share/69cd6dd0-91e4-832f-a70b-93808619faf5 more troubleshooting for the styling
https://chatgpt.com/share/69d7d40d-e0c4-8328-9098-7841609310c7 I had an error about routes for the update user sites 
https://chatgpt.com/share/69d7d421-29ac-832d-adb9-c3d86e5a3498 This was about 404 errors when creating the routes
https://chatgpt.com/share/69d7d46e-c26c-8328-85ca-c05d61a3a979 
https://chatgpt.com/share/69d7d47f-47d8-8328-a1a5-6fe48d6e01c5 a 404 error about the routes
https://chatgpt.com/share/69d7d492-99bc-8325-9b27-2045b6e0a4f8 this was for making the sql database because making a rds database was outside the scope of the class
https://chatgpt.com/share/69d7d4b8-7f98-832a-bbd4-88717c5a9a23 asking if it would be possible to click names for different sites
https://chatgpt.com/share/69d7d4d2-790c-832a-ae4f-f1f098f385c3 Styles for bootstrap and css were clashing
https://chatgpt.com/share/69cd6dd0-91e4-832f-a70b-93808619faf5 Fixing styles because bootstrap and css were overriding each other
https://chatgpt.com/share/69d7d51c-4498-8332-bdfe-29b1b672973f same with this