## 🚀 Submission Format
For each playlist in the challenge set, participants will submit a ranked list of 500 recommended track URIs. The file format should be a gzipped csv (.csv.gz) file. The order of the recommended tracks matters: more relevant recommendations should appear first in the list. Submissions should be made in the following comma-separated format:

* All fields are comma separated. It is OK but optional to have whitespace before and after the comma.
* Comments are allowed with a '#' at the beginning of a line.
* Empty lines are OK (they are ignored).
* The first non-commented/blank line must start with "team_info" and then include the team name, and a contact email address. (Note: If you previously participated in the RecSys Challenge 2018, there was an additional field specifying "main" or "creative" track. Since this challenge only has one track, that field has been removed from the first line.) Example:
> team_info, my awesome team name, my_awesome_team@email.com

* For each challenge playlist there must be a line of the form

> pid, trackuri_1, trackuri_2, trackuri_3, ..., trackuri_499, trackuri_500
with exactly 500 tracks.

### Important note about submissions:
* The seed tracks, provided as part of the challenge set, must not be included in the submission.
* The submission for any particular playlist must not contain duplicated tracks.
* A submission must contain exactly 500 tracks (post deduplication).
* Any submission violating one of the formatting rules will be rejected by the scoring system.

A sample submission (sample_submission.csv) is included with the challenge set. The sample shows the expected format for your submission to the challenge. Also included with the challenge set is a Python script called verify_submission.py. You can use this program to verify that your submission is properly formatted. See the challenge set README file for more information on how to verify and submit your challenge results.