### Additions to continue:
- Add emails to all other steps. 
  At the moment it only works as a reminder to the appointment chairman. 
  Consult with Nitzan about which users/officials will receive the email at each stage.
- In the candidate file - add a button that will combine all the files into one file and download them combined into a single file
  + completing the rest of the buttons in the table of the candidate file (some of them are inactive, it is necessary to consult with Nitzan regarding their definitions).
- Adding a comments window in a candidate's file according to Figma. Comments related to the candidate are saved in a json file in the Applications table. 
  Each comment is associated with a file, so when adding comments to a candidate's file, you should add an option of general comments in json or elsewhere of your choice.
- The eye marking in the table of all notifications on the home page is inactive and you need to consult with Nitzan about whether it is relevant and necessary.

### Finally 
- Completion of the other users pages except the admin.

### Remarks:
- The page-admin folder contains all the admin pages.
- Saving files - there are several types of documents that are listed in constants.js that as soon as a file is added,
  the type of file is added to the json of the request in the Applications table and three fields are added to it:
  - URL - the address of the file
  - uploadWith- the name of the user who uploaded the file.
  - date – its upload date.
    Notes are saved so that a notes field is added and the note added to it.

   ### pay attention! 
   When uploading a CV or Initiative Letter in the new applications stage, 
   they are saved together within the CV& Initiative Letter type and their comments are saved as one common comment.
