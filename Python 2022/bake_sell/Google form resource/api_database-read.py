{
  "mtlsRootUrl": "https://forms.mtls.googleapis.com/",
  "servicePath": "",
  "documentationLink": "https://developers.google.com/forms/api",
  "id": "forms:v1",
##########################################################################################################################################################################################################
  "schemas": {
    "DateQuestion": {
      "id": "DateQuestion",
      "description": "A date question. Date questions default to just month + day.",
      "properties": {
        "includeYear": {
          "type": "boolean",
          "description": "Whether to include the year as part of the question."
        },
        "includeTime": {
          "type": "boolean",
          "description": "Whether to include the time as part of the question."
        }
      },
      "type": "object"
    },
##########################################################################################################################################################################################################
    "Grading": {
      "id": "Grading",
      "properties": {
        "correctAnswers": {
          "description": "Required. The answer key for the question. Responses are automatically graded based on this field.",
          "$ref": "CorrectAnswers"
        },
        "whenRight": {
          "description": "The feedback displayed for correct responses. This feedback can only be set for multiple choice questions that have correct answers provided.",
          "$ref": "Feedback"
        },
        "whenWrong": {
          "$ref": "Feedback",
          "description": "The feedback displayed for incorrect responses. This feedback can only be set for multiple choice questions that have correct answers provided."
        },
        "generalFeedback": {
          "$ref": "Feedback",
          "description": "The feedback displayed for all answers. This is commonly used for short answer questions when a quiz owner wants to quickly give respondents some sense of whether they answered the question correctly before they've had a chance to officially grade the response. General feedback cannot be set for automatically graded multiple choice questions."
        },
        "pointValue": {
          "format": "int32",
          "description": "Required. The maximum number of points a respondent can automatically get for a correct answer. This must not be negative.",
          "type": "integer"
        }
      },
      "type": "object",
      "description": "Grading for a single question"
    },
##########################################################################################################################################################################################################
    "CorrectAnswer": {
      "type": "object",
      "description": "A single correct answer for a question. For multiple-valued (`CHECKBOX`) questions, several `CorrectAnswer`s may be needed to represent a single correct response option.",
      "properties": {
        "value": {
          "type": "string",
          "description": "Required. The correct answer value. See the documentation for TextAnswer.value for details on how various value types are formatted."
        }
      },
      "id": "CorrectAnswer"
    },
##########################################################################################################################################################################################################
    "Location": {
      "id": "Location",
      "type": "object",
      "description": "A specific location in a form.",
      "properties": {
        "index": {
          "type": "integer",
          "format": "int32",
          "description": "The index of an item in the form. This must be in the range [0..*N*), where *N* is the number of items in the form."
        }
      }
    },
##########################################################################################################################################################################################################
    "TimeQuestion": {
      "type": "object",
      "id": "TimeQuestion",
      "properties": {
        "duration": {
          "type": "boolean",
          "description": "`true` if the question is about an elapsed time. Otherwise it is about a time of day."
        }
      },
      "description": "A time question."
    },
##########################################################################################################################################################################################################
    "Video": {
      "id": "Video",
      "description": "Data representing a video.",
      "properties": {
        "youtubeUri": {
          "type": "string",
          "description": "Required. A YouTube URI."
        },
        "properties": {
          "description": "Properties of a video.",
          "$ref": "MediaProperties"
        }
      },
      "type": "object"
    },
##########################################################################################################################################################################################################
    "CorrectAnswers": {
      "properties": {
        "answers": {
          "type": "array",
          "items": {
            "$ref": "CorrectAnswer"
          },
          "description": "A list of correct answers. A quiz response can be automatically graded based on these answers. For single-valued questions, a response is marked correct if it matches any value in this list (in other words, multiple correct answers are possible). For multiple-valued (`CHECKBOX`) questions, a response is marked correct if it contains exactly the values in this list."
        }
      },
      "id": "CorrectAnswers",
      "type": "object",
      "description": "The answer key for a question."
    },
##########################################################################################################################################################################################################
    "FileUploadAnswer": {
      "type": "object",
      "id": "FileUploadAnswer",
      "description": "Info for a single file submitted to a file upload question.",
      "properties": {
        "fileId": {
          "type": "string",
          "description": "Output only. The ID of the Google Drive file.",
          "readOnly": true
        },
        "fileName": {
          "type": "string",
          "description": "Output only. The file name, as stored in Google Drive on upload.",
          "readOnly": true
        },
        "mimeType": {
          "description": "Output only. The MIME type of the file, as stored in Google Drive on upload.",
          "type": "string",
          "readOnly": true
        }
      }
    },
##########################################################################################################################################################################################################
    "Info": {
      "properties": {
        "documentTitle": {
          "readOnly": true,
          "description": "Output only. The title of the document which is visible in Drive. If `Info.title` is empty, `document_title` may appear in its place in the Google Forms UI and be visible to responders. `document_title` can be set on create, but cannot be modified by a batchUpdate request. Please use the [Google Drive API](https://developers.google.com/drive/api/v3/reference/files/update) if you need to programmatically update `document_title`.",
          "type": "string"
        },
        "title": {
          "description": "Required. The title of the form which is visible to responders.",
          "type": "string"
        },
        "description": {
          "type": "string",
          "description": "The description of the form."
        }
      },
      "type": "object",
      "id": "Info",
      "description": "The general information for a form."
    },
##########################################################################################################################################################################################################
    "ScaleQuestion": {
      "properties": {
        "lowLabel": {
          "description": "The label to display describing the lowest point on the scale.",
          "type": "string"
        },
        "low": {
          "format": "int32",
          "type": "integer",
          "description": "Required. The lowest possible value for the scale."
        },
        "highLabel": {
          "description": "The label to display describing the highest point on the scale.",
          "type": "string"
        },
        "high": {
          "type": "integer",
          "format": "int32",
          "description": "Required. The highest possible value for the scale."
        }
      },
      "type": "object",
      "id": "ScaleQuestion",
      "description": "A scale question. The user has a range of numeric values to choose from."
    },
##########################################################################################################################################################################################################
    "QuizSettings": {
      "properties": {
        "isQuiz": {
          "type": "boolean",
          "description": "Whether this form is a quiz or not. When true, responses are graded based on question Grading. Upon setting to false, all question Grading is deleted."
        }
      },
      "id": "QuizSettings",
      "description": "Settings related to quiz forms and grading. These must be updated with the UpdateSettingsRequest.",
      "type": "object"
    },
##########################################################################################################################################################################################################
    "Image": {
      "description": "Data representing an image.",
      "properties": {
        "sourceUri": {
          "description": "Input only. The source URI is the URI used to insert the image. The source URI can be empty when fetched.",
          "type": "string"
        },
        "contentUri": {
          "readOnly": true,
          "description": "Output only. A URI from which you can download the image; this is valid only for a limited time.",
          "type": "string"
        },
        "properties": {
          "$ref": "MediaProperties",
          "description": "Properties of an image."
        },
        "altText": {
          "type": "string",
          "description": "A description of the image that is shown on hover and read by screenreaders."
        }
      },
      "id": "Image",
      "type": "object"
    },
##########################################################################################################################################################################################################
    "FormResponse": {
      "id": "FormResponse",
      "properties": {
        "totalScore": {
          "description": "Output only. The total number of points the respondent received for their submission Only set if the form was a quiz and the response was graded. This includes points automatically awarded via autograding adjusted by any manual corrections entered by the form owner.",
          "format": "double",
          "type": "number",
          "readOnly": true
        },
        "responseId": {
          "description": "Output only. The response ID.",
          "readOnly": true,
          "type": "string"
        },
        "createTime": {
          "type": "string",
          "readOnly": true,
          "format": "google-datetime",
          "description": "Output only. Timestamp for the first time the response was submitted."
        },
        "formId": {
          "readOnly": true,
          "description": "Output only. The form ID.",
          "type": "string"
        },
        "respondentEmail": {
          "type": "string",
          "readOnly": true,
          "description": "Output only. The email address (if collected) for the respondent."
        },
        "lastSubmittedTime": {
          "type": "string",
          "format": "google-datetime",
          "description": "Output only. Timestamp for the most recent time the response was submitted. Does not track changes to grades.",
          "readOnly": true
        },
        "answers": {
          "description": "Output only. The actual answers to the questions, keyed by question_id.",
          "type": "object",
          "additionalProperties": {
            "$ref": "Answer"
          },
          "readOnly": true
        }
      },
      "type": "object",
      "description": "A form response."
    },
##########################################################################################################################################################################################################
    "Grade": {
      "id": "Grade",
      "properties": {
        "score": {
          "type": "number",
          "readOnly": true,
          "description": "Output only. The numeric score awarded for the answer.",
          "format": "double"
        },
        "feedback": {
          "$ref": "Feedback",
          "description": "Output only. Additional feedback given for an answer.",
          "readOnly": true
        },
        "correct": {
          "readOnly": true,
          "description": "Output only. Whether the question was answered correctly or not. A zero-point score is not enough to infer incorrectness, since a correctly answered question could be worth zero points.",
          "type": "boolean"
        }
      },
      "type": "object",
      "description": "Grade information associated with a respondent's answer to a question."
    },
##########################################################################################################################################################################################################
    "FormSettings": {
      "id": "FormSettings",
      "description": "A form's settings.",
      "type": "object",
      "properties": {
        "quizSettings": {
          "$ref": "QuizSettings",
          "description": "Settings related to quiz forms and grading."
        }
      }
    },
##########################################################################################################################################################################################################
    "Option": {
      "description": "An option for a Choice question.",
      "id": "Option",
      "type": "object",
      "properties": {
        "image": {
          "description": "Display image as an option.",
          "$ref": "Image"
        },
        "goToSectionId": {
          "description": "Item ID of section header to go to.",
          "type": "string"
        },
        "goToAction": {
          "description": "Section navigation type.",
          "enumDescriptions": [
            "Default value. Unused.",
            "Go to the next section.",
            "Go back to the beginning of the form.",
            "Submit form immediately."
          ],
          "type": "string",
          "enum": [
            "GO_TO_ACTION_UNSPECIFIED",
            "NEXT_SECTION",
            "RESTART_FORM",
            "SUBMIT_FORM"
          ]
        },
        "isOther": {
          "type": "boolean",
          "description": "Whether the option is \"other\". Currently only applies to `RADIO` and `CHECKBOX` choice types, but is not allowed in a QuestionGroupItem."
        },
        "value": {
          "type": "string",
          "description": "Required. The choice as presented to the user."
        }
      }
    },
##########################################################################################################################################################################################################
    "Question": {
      "properties": {
        "textQuestion": {
          "description": "A respondent can enter a free text response.",
          "$ref": "TextQuestion"
        },
        "choiceQuestion": {
          "$ref": "ChoiceQuestion",
          "description": "A respondent can choose from a pre-defined set of options."
        },
        "timeQuestion": {
          "$ref": "TimeQuestion",
          "description": "A respondent can enter a time."
        },
        "required": {
          "type": "boolean",
          "description": "Whether the question must be answered in order for a respondent to submit their response."
        },
        "grading": {
          "description": "Grading setup for the question.",
          "$ref": "Grading"
        },
        "rowQuestion": {
          "$ref": "RowQuestion",
          "description": "A row of a QuestionGroupItem."
        },
        "questionId": {
          "description": "Read only. The question ID. On creation, it can be provided but the ID must not be already used in the form. If not provided, a new ID is assigned.",
          "type": "string"
        },
        "fileUploadQuestion": {
          "$ref": "FileUploadQuestion",
          "description": "A respondent can upload one or more files."
        },
        "scaleQuestion": {
          "$ref": "ScaleQuestion",
          "description": "A respondent can choose a number from a range."
        },
        "dateQuestion": {
          "description": "A respondent can enter a date.",
          "$ref": "DateQuestion"
        }
      },
      "description": "Any question. The specific type of question is known by its `kind`.",
      "type": "object",
      "id": "Question"
    },
##########################################################################################################################################################################################################
    "Grid": {
      "id": "Grid",
      "description": "A grid of choices (radio or check boxes) with each row constituting a separate question. Each row has the same choices, which are shown as the columns.",
      "properties": {
        "shuffleQuestions": {
          "description": "If `true`, the questions are randomly ordered. In other words, the rows appear in a different order for every respondent.",
          "type": "boolean"
        },
        "columns": {
          "$ref": "ChoiceQuestion",
          "description": "Required. The choices shared by each question in the grid. In other words, the values of the columns. Only `CHECK_BOX` and `RADIO` choices are allowed."
        }
      },
      "type": "object"
    },
##########################################################################################################################################################################################################
    "Watch": {
      "id": "Watch",
      "description": "A watch for events for a form. When the designated event happens, a notification will be published to the specified target. The notification's attributes will include a `formId` key that has the ID of the watched form and an `eventType` key that has the string of the type. Messages are sent with at-least-once delivery and are only dropped in extraordinary circumstances. Typically all notifications should be reliably delivered within a few seconds; however, in some situations notifications may be delayed. A watch expires seven days after it is created unless it is renewed with watches.renew",
      "properties": {
        "expireTime": {
          "description": "Output only. Timestamp for when this will expire. Each watches.renew call resets this to seven days in the future.",
          "format": "google-datetime",
          "readOnly": true,
          "type": "string"
        },
        "createTime": {
          "type": "string",
          "readOnly": true,
          "description": "Output only. Timestamp of when this was created.",
          "format": "google-datetime"
        },
        "errorType": {
          "enumDescriptions": [
            "Unspecified error type.",
            "The cloud project does not have access to the form being watched. This occurs if the user has revoked the authorization for your project to access their form(s). Watches with this error will not be retried. To attempt to begin watching the form again a call can be made to watches.renew",
            "The user that granted access no longer has access to the form being watched. Watches with this error will not be retried. To attempt to begin watching the form again a call can be made to watches.renew",
            "Another type of error has occurred. Whether notifications will continue depends on the watch state."
          ],
          "enum": [
            "ERROR_TYPE_UNSPECIFIED",
            "PROJECT_NOT_AUTHORIZED",
            "NO_USER_ACCESS",
            "OTHER_ERRORS"
          ],
          "description": "Output only. The most recent error type for an attempted delivery. To begin watching the form again a call can be made to watches.renew which also clears this error information.",
          "type": "string",
          "readOnly": true
        },
        "id": {
          "type": "string",
          "readOnly": true,
          "description": "Output only. The ID of this watch. See notes on CreateWatchRequest.watch_id."
        },
        "state": {
          "description": "Output only. The current state of the watch. Additional details about suspended watches can be found by checking the `error_type`.",
          "enum": [
            "STATE_UNSPECIFIED",
            "ACTIVE",
            "SUSPENDED"
          ],
          "enumDescriptions": [
            "Unspecified state.",
            "Watch is active.",
            "The watch is suspended due to an error that may be resolved. The watch will continue to exist until it expires. To attempt to reactivate the watch a call can be made to watches.renew"
          ],
          "type": "string",
          "readOnly": true
        },
        "target": {
          "$ref": "WatchTarget",
          "description": "Required. Where to send the notification."
        },
        "eventType": {
          "enumDescriptions": [
            "Unspecified event type. This value should not be used.",
            "The schema event type. A watch with this event type will be notified about changes to form content and settings.",
            "The responses event type. A watch with this event type will be notified when form responses are submitted."
          ],
          "enum": [
            "EVENT_TYPE_UNSPECIFIED",
            "SCHEMA",
            "RESPONSES"
          ],
          "description": "Required. Which event type to watch for.",
          "type": "string"
        }
      },
      "type": "object"
    },
##########################################################################################################################################################################################################
    "UpdateSettingsRequest": {
      "id": "UpdateSettingsRequest",
      "type": "object",
      "properties": {
        "updateMask": {
          "format": "google-fieldmask",
          "description": "Required. Only values named in this mask are changed. At least one field must be specified. The root `settings` is implied and should not be specified. A single `\"*\"` can be used as short-hand for updating every field.",
          "type": "string"
        },
        "settings": {
          "description": "Required. The settings to update with.",
          "$ref": "FormSettings"
        }
      },
      "description": "Update Form's FormSettings."
    },
##########################################################################################################################################################################################################
    "CloudPubsubTopic": {
      "properties": {
        "topicName": {
          "description": "Required. A fully qualified Pub/Sub topic name to publish the events to. This topic must be owned by the calling project and already exist in Pub/Sub.",
          "type": "string"
        }
      },
      "description": "A Pub/Sub topic.",
      "id": "CloudPubsubTopic",
      "type": "object"
    },
    "QuestionGroupItem": {
      "description": "Defines a question that comprises multiple questions grouped together.",
      "type": "object",
      "id": "QuestionGroupItem",
      "properties": {
        "image": {
          "$ref": "Image",
          "description": "The image displayed within the question group above the specific questions."
        },
        "questions": {
          "description": "Required. A list of questions that belong in this question group. A question must only belong to one group. The `kind` of the group may affect what types of questions are allowed.",
          "items": {
            "$ref": "Question"
          },
          "type": "array"
        },
        "grid": {
          "description": "The question group is a grid with rows of multiple choice questions that share the same options. When `grid` is set, all questions in the group must be of kind `row`.",
          "$ref": "Grid"
        }
      }
    },
##########################################################################################################################################################################################################
    "RenewWatchRequest": {
      "type": "object",
      "description": "Renew an existing Watch for seven days.",
      "properties": {},
      "id": "RenewWatchRequest"
    },
##########################################################################################################################################################################################################
    "TextAnswers": {
      "description": "A question's answers as text.",
      "id": "TextAnswers",
      "type": "object",
      "properties": {
        "answers": {
          "type": "array",
          "description": "Output only. Answers to a question. For multiple-value ChoiceQuestions, each answer is a separate value.",
          "items": {
            "$ref": "TextAnswer"
          },
          "readOnly": true
        }
      }
    },
##########################################################################################################################################################################################################
    "TextItem": {
      "properties": {},
      "description": "A text item.",
      "type": "object",
      "id": "TextItem"
    },
##########################################################################################################################################################################################################
    "CreateItemResponse": {
      "properties": {
        "questionId": {
          "description": "The ID of the question created as part of this item, for a question group it lists IDs of all the questions created for this item.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "itemId": {
          "type": "string",
          "description": "The ID of the created item."
        }
      },
      "description": "The result of creating an item.",
      "id": "CreateItemResponse",
      "type": "object"
    },
##########################################################################################################################################################################################################
    "BatchUpdateFormRequest": {
      "type": "object",
      "description": "A batch of updates to perform on a form. All the specified updates are made or none of them are.",
      "id": "BatchUpdateFormRequest",
      "properties": {
        "includeFormInResponse": {
          "description": "Whether to return an updated version of the model in the response.",
          "type": "boolean"
        },
        "requests": {
          "description": "Required. The update requests of this batch.",
          "items": {
            "$ref": "Request"
          },
          "type": "array"
        },
        "writeControl": {
          "description": "Provides control over how write requests are executed.",
          "$ref": "WriteControl"
        }
      }
    },
##########################################################################################################################################################################################################
    "ChoiceQuestion": {
      "description": "A radio/checkbox/dropdown question.",
      "type": "object",
      "properties": {
        "shuffle": {
          "description": "Whether the options should be displayed in random order for different instances of the quiz. This is often used to prevent cheating by respondents who might be looking at another respondent's screen, or to address bias in a survey that might be introduced by always putting the same options first or last.",
          "type": "boolean"
        },
        "options": {
          "type": "array",
          "description": "Required. List of options that a respondent must choose from.",
          "items": {
            "$ref": "Option"
          }
        },
        "type": {
          "type": "string",
          "enum": [
            "CHOICE_TYPE_UNSPECIFIED",
            "RADIO",
            "CHECKBOX",
            "DROP_DOWN"
          ],
          "description": "Required. The type of choice question.",
          "enumDescriptions": [
            "Default value. Unused.",
            "Radio buttons: All choices are shown to the user, who can only pick one of them.",
            "Checkboxes: All choices are shown to the user, who can pick any number of them.",
            "Drop-down menu: The choices are only shown to the user on demand, otherwise only the current choice is shown. Only one option can be chosen."
          ]
        }
      },
      "id": "ChoiceQuestion"
    },
##########################################################################################################################################################################################################
    "MoveItemRequest": {
      "properties": {
        "originalLocation": {
          "description": "Required. The location of the item to move.",
          "$ref": "Location"
        },
        "newLocation": {
          "description": "Required. The new location for the item.",
          "$ref": "Location"
        }
      },
      "type": "object",
      "id": "MoveItemRequest",
      "description": "Move an item in a form."
    },
##########################################################################################################################################################################################################
    "Item": {
      "type": "object",
      "properties": {
        "itemId": {
          "description": "The item ID. On creation, it can be provided but the ID must not be already used in the form. If not provided, a new ID is assigned.",
          "type": "string"
        },
        "textItem": {
          "$ref": "TextItem",
          "description": "Displays a title and description on the page."
        },
        "questionGroupItem": {
          "description": "Poses one or more questions to the user with a single major prompt.",
          "$ref": "QuestionGroupItem"
        },
        "title": {
          "description": "The title of the item.",
          "type": "string"
        },
        "description": {
          "description": "The description of the item.",
          "type": "string"
        },
        "videoItem": {
          "$ref": "VideoItem",
          "description": "Displays a video on the page."
        },
        "pageBreakItem": {
          "description": "Starts a new page with a title.",
          "$ref": "PageBreakItem"
        },
        "imageItem": {
          "$ref": "ImageItem",
          "description": "Displays an image on the page."
        },
        "questionItem": {
          "$ref": "QuestionItem",
          "description": "Poses a question to the user."
        }
      },
      "description": "A single item of the form. `kind` defines which kind of item it is.",
      "id": "Item"
    },
##########################################################################################################################################################################################################
    "CreateItemRequest": {
      "type": "object",
      "properties": {
        "item": {
          "$ref": "Item",
          "description": "Required. The item to create."
        },
        "location": {
          "description": "Required. Where to place the new item.",
          "$ref": "Location"
        }
      },
      "id": "CreateItemRequest",
      "description": "Create an item in a form."
    },
##########################################################################################################################################################################################################
    "ListFormResponsesResponse": {
      "type": "object",
      "description": "Response to a ListFormResponsesRequest.",
      "properties": {
        "nextPageToken": {
          "description": "If set, there are more responses. To get the next page of responses, provide this as `page_token` in a future request.",
          "type": "string"
        },
        "responses": {
          "type": "array",
          "items": {
            "$ref": "FormResponse"
          },
          "description": "The returned responses."
        }
      },
      "id": "ListFormResponsesResponse"
    },
##########################################################################################################################################################################################################
    "Request": {
      "properties": {
        "deleteItem": {
          "description": "Delete an item.",
          "$ref": "DeleteItemRequest"
        },
        "updateItem": {
          "description": "Update an item.",
          "$ref": "UpdateItemRequest"
        },
        "updateFormInfo": {
          "description": "Update Form's Info.",
          "$ref": "UpdateFormInfoRequest"
        },
        "createItem": {
          "$ref": "CreateItemRequest",
          "description": "Create a new item."
        },
        "updateSettings": {
          "description": "Updates the Form's settings.",
          "$ref": "UpdateSettingsRequest"
        },
        "moveItem": {
          "$ref": "MoveItemRequest",
          "description": "Move an item to a specified location."
        }
      },
      "id": "Request",
      "description": "The kinds of update requests that can be made.",
      "type": "object"
    },
##########################################################################################################################################################################################################
    "FileUploadQuestion": {
      "description": "A file upload question. The API currently does not support creating file upload questions.",
      "id": "FileUploadQuestion",
      "properties": {
        "folderId": {
          "description": "Required. The ID of the Drive folder where uploaded files are stored.",
          "type": "string"
        },
        "types": {
          "description": "File types accepted by this question.",
          "items": {
            "enum": [
              "FILE_TYPE_UNSPECIFIED",
              "ANY",
              "DOCUMENT",
              "PRESENTATION",
              "SPREADSHEET",
              "DRAWING",
              "PDF",
              "IMAGE",
              "VIDEO",
              "AUDIO"
            ],
            "enumDescriptions": [
              "Default value. Unused.",
              "No restrictions on type.",
              "A Google Docs document.",
              "A Google Slides presentation.",
              "A Google Sheets spreadsheet.",
              "A drawing.",
              "A PDF.",
              "An image.",
              "A video.",
              "An audio file."
            ],
            "type": "string"
          },
          "type": "array"
        },
        "maxFileSize": {
          "type": "string",
          "format": "int64",
          "description": "Maximum number of bytes allowed for any single file uploaded to this question."
        },
        "maxFiles": {
          "description": "Maximum number of files that can be uploaded for this question in a single response.",
          "format": "int32",
          "type": "integer"
        }
      },
      "type": "object"
    },
##########################################################################################################################################################################################################
    "UpdateItemRequest": {
      "description": "Update an item in a form.",
      "properties": {
        "updateMask": {
          "description": "Required. Only values named in this mask are changed.",
          "format": "google-fieldmask",
          "type": "string"
        },
        "item": {
          "$ref": "Item",
          "description": "Required. New values for the item. Note that item and question IDs are used if they are provided (and are in the field mask). If an ID is blank (and in the field mask) a new ID is generated. This means you can modify an item by getting the form via forms.get, modifying your local copy of that item to be how you want it, and using UpdateItemRequest to write it back, with the IDs being the same (or not in the field mask)."
        },
        "location": {
          "description": "Required. The location identifying the item to update.",
          "$ref": "Location"
        }
      },
      "id": "UpdateItemRequest",
      "type": "object"
    },
##########################################################################################################################################################################################################
    "WriteControl": {
      "properties": {
        "requiredRevisionId": {
          "type": "string",
          "description": "The revision ID of the form that the write request is applied to. If this is not the latest revision of the form, the request is not processed and returns a 400 bad request error."
        },
        "targetRevisionId": {
          "type": "string",
          "description": "The target revision ID of the form that the write request is applied to. If changes have occurred after this revision, the changes in this update request are transformed against those changes. This results in a new revision of the form that incorporates both the changes in the request and the intervening changes, with the server resolving conflicting changes. The target revision ID may only be used to write to recent versions of a form. If the target revision is too far behind the latest revision, the request is not processed and returns a 400 (Bad Request Error). The request may be retried after reading the latest version of the form. In most cases a target revision ID remains valid for several minutes after it is read, but for frequently-edited forms this window may be shorter."
        }
      },
      "description": "Provides control over how write requests are executed.",
      "id": "WriteControl",
      "type": "object"
    },
##########################################################################################################################################################################################################
    "UpdateFormInfoRequest": {
      "description": "Update Form's Info.",
      "properties": {
        "info": {
          "description": "The info to update.",
          "$ref": "Info"
        },
        "updateMask": {
          "description": "Required. Only values named in this mask are changed. At least one field must be specified. The root `info` is implied and should not be specified. A single `\"*\"` can be used as short-hand for updating every field.",
          "format": "google-fieldmask",
          "type": "string"
        }
      },
      "id": "UpdateFormInfoRequest",
      "type": "object"
    },
##########################################################################################################################################################################################################
    "PageBreakItem": {
      "type": "object",
      "description": "A page break. The title and description of this item are shown at the top of the new page.",
      "properties": {},
      "id": "PageBreakItem"
    },
##########################################################################################################################################################################################################
    "QuestionItem": {
      "type": "object",
      "id": "QuestionItem",
      "properties": {
        "question": {
          "description": "Required. The displayed question.",
          "$ref": "Question"
        },
        "image": {
          "description": "The image displayed within the question.",
          "$ref": "Image"
        }
      },
      "description": "A form item containing a single question."
    },
##########################################################################################################################################################################################################
    "RowQuestion": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "Required. The title for the single row in the QuestionGroupItem."
        }
      },
      "id": "RowQuestion",
      "description": "Configuration for a question that is part of a question group."
    },
##########################################################################################################################################################################################################
    "BatchUpdateFormResponse": {
      "id": "BatchUpdateFormResponse",
      "type": "object",
      "properties": {
        "writeControl": {
          "$ref": "WriteControl",
          "description": "The updated write control after applying the request."
        },
        "replies": {
          "description": "The reply of the updates. This maps 1:1 with the update requests, although replies to some requests may be empty.",
          "type": "array",
          "items": {
            "$ref": "Response"
          }
        },
        "form": {
          "$ref": "Form",
          "description": "Based on the bool request field `include_form_in_response`, a form with all applied mutations/updates is returned or not. This may be later than the revision ID created by these changes."
        }
      },
      "description": "Response to a BatchUpdateFormRequest."
    },
##########################################################################################################################################################################################################
    "VideoLink": {
      "description": "Link to a video.",
      "type": "object",
      "id": "VideoLink",
      "properties": {
        "displayText": {
          "type": "string",
          "description": "Required. The display text for the link."
        },
        "youtubeUri": {
          "type": "string",
          "description": "The URI of a YouTube video."
        }
      }
    },
##########################################################################################################################################################################################################
    "ExtraMaterial": {
      "description": "Supplementary material to the feedback.",
      "id": "ExtraMaterial",
      "type": "object",
      "properties": {
        "link": {
          "description": "Text feedback.",
          "$ref": "TextLink"
        },
        "video": {
          "$ref": "VideoLink",
          "description": "Video feedback."
        }
      }
    },
##########################################################################################################################################################################################################
    "VideoItem": {
      "id": "VideoItem",
      "properties": {
        "video": {
          "$ref": "Video",
          "description": "Required. The video displayed in the item."
        },
        "caption": {
          "type": "string",
          "description": "The text displayed below the video."
        }
      },
      "type": "object",
      "description": "An item containing a video."
    },
##########################################################################################################################################################################################################
    "Response": {
      "id": "Response",
      "description": "A single response from an update.",
      "type": "object",
      "properties": {
        "createItem": {
          "$ref": "CreateItemResponse",
          "description": "The result of creating an item."
        }
      }
    },
##########################################################################################################################################################################################################
    "TextQuestion": {
      "type": "object",
      "description": "A text-based question.",
      "properties": {
        "paragraph": {
          "type": "boolean",
          "description": "Whether the question is a paragraph question or not. If not, the question is a short text question."
        }
      },
      "id": "TextQuestion"
    },
##########################################################################################################################################################################################################
    "ListWatchesResponse": {
      "description": "The response of a ListWatchesRequest.",
      "id": "ListWatchesResponse",
      "properties": {
        "watches": {
          "description": "The returned watches.",
          "type": "array",
          "items": {
            "$ref": "Watch"
          }
        }
      },
      "type": "object"
    },
##########################################################################################################################################################################################################
    "WatchTarget": {
      "properties": {
        "topic": {
          "$ref": "CloudPubsubTopic",
          "description": "A Pub/Sub topic. To receive notifications, the topic must grant publish privileges to the Forms service account `serviceAccount:forms-notifications@system.gserviceaccount.com`. Only the project that owns a topic may create a watch with it. Pub/Sub delivery guarantees should be considered."
        }
      },
      "type": "object",
      "id": "WatchTarget",
      "description": "The target for notification delivery."
    },
##########################################################################################################################################################################################################
    "CreateWatchRequest": {
      "description": "Create a new watch.",
      "id": "CreateWatchRequest",
      "properties": {
        "watch": {
          "$ref": "Watch",
          "description": "Required. The watch object. No ID should be set on this object; use `watch_id` instead."
        },
        "watchId": {
          "type": "string",
          "description": "The ID to use for the watch. If specified, the ID must not already be in use. If not specified, an ID is generated. This value should be 4-63 characters, and valid characters are /a-z-/."
        }
      },
      "type": "object"
    },
##########################################################################################################################################################################################################
    "TextLink": {
      "id": "TextLink",
      "properties": {
        "displayText": {
          "type": "string",
          "description": "Required. Display text for the URI."
        },
        "uri": {
          "description": "Required. The URI.",
          "type": "string"
        }
      },
      "description": "Link for text.",
      "type": "object"
    },
##########################################################################################################################################################################################################
    "ImageItem": {
      "type": "object",
      "properties": {
        "image": {
          "$ref": "Image",
          "description": "Required. The image displayed in the item."
        }
      },
      "id": "ImageItem",
      "description": "An item containing an image."
    },
##########################################################################################################################################################################################################
    "Answer": {
      "properties": {
        "textAnswers": {
          "$ref": "TextAnswers",
          "description": "Output only. The specific answers as text.",
          "readOnly": true
        },
        "grade": {
          "$ref": "Grade",
          "readOnly": true,
          "description": "Output only. The grade for the answer if the form was a quiz."
        },
        "questionId": {
          "readOnly": true,
          "description": "Output only. The question's ID. See also Question.question_id.",
          "type": "string"
        },
        "fileUploadAnswers": {
          "readOnly": true,
          "$ref": "FileUploadAnswers",
          "description": "Output only. The answers to a file upload question."
        }
      },
      "description": "The submitted answer for a question.",
      "type": "object",
      "id": "Answer"
    },
##########################################################################################################################################################################################################
    "MediaProperties": {
      "properties": {
        "width": {
          "format": "int32",
          "type": "integer",
          "description": "The width of the media in pixels. When the media is displayed, it is scaled to the smaller of this value or the width of the displayed form. The original aspect ratio of the media is preserved. If a width is not specified when the media is added to the form, it is set to the width of the media source. Width must be between 0 and 740, inclusive. Setting width to 0 or unspecified is only permitted when updating the media source."
        },
        "alignment": {
          "enumDescriptions": [
            "Default value. Unused.",
            "Left align.",
            "Right align.",
            "Center."
          ],
          "enum": [
            "ALIGNMENT_UNSPECIFIED",
            "LEFT",
            "RIGHT",
            "CENTER"
          ],
          "type": "string",
          "description": "Position of the media."
        }
      },
      "id": "MediaProperties",
      "description": "Properties of the media.",
      "type": "object"
    },
##########################################################################################################################################################################################################
    "Form": {
      "type": "object",
      "id": "Form",
      "properties": {
        "revisionId": {
          "readOnly": true,
          "type": "string",
          "description": "Output only. The revision ID of the form. Used in the WriteControl in update requests to identify the revision on which the changes are based. The format of the revision ID may change over time, so it should be treated opaquely. A returned revision ID is only guaranteed to be valid for 24 hours after it has been returned and cannot be shared across users. If the revision ID is unchanged between calls, then the form has not changed. Conversely, a changed ID (for the same form and user) usually means the form has been updated; however, a changed ID can also be due to internal factors such as ID format changes."
        },
        "items": {
          "description": "Required. A list of the form's items, which can include section headers, questions, embedded media, etc.",
          "type": "array",
          "items": {
            "$ref": "Item"
          }
        },
        "formId": {
          "readOnly": true,
          "type": "string",
          "description": "Output only. The form ID."
        },
        "responderUri": {
          "type": "string",
          "description": "Output only. The form URI to share with responders. This opens a page that allows the user to submit responses but not edit the questions.",
          "readOnly": true
        },
        "info": {
          "$ref": "Info",
          "description": "Required. The title and description of the form."
        },
        "settings": {
          "$ref": "FormSettings",
          "description": "The form's settings. This must be updated with UpdateSettingsRequest; it is ignored during `forms.create` and UpdateFormInfoRequest."
        },
        "linkedSheetId": {
          "description": "Output only. The ID of the linked Google Sheet which is accumulating responses from this Form (if such a Sheet exists).",
          "type": "string",
          "readOnly": true
        }
      },
      "description": "A Google Forms document. A form is created in Drive, and deleting a form or changing its access protections is done via the [Drive API](https://developers.google.com/drive/api/v3/about-sdk)."
    },
##########################################################################################################################################################################################################
    "Empty": {
      "type": "object",
      "id": "Empty",
      "properties": {},
      "description": "A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }"
    },
##########################################################################################################################################################################################################
    "DeleteItemRequest": {
      "description": "Delete an item in a form.",
      "properties": {
        "location": {
          "description": "Required. The location of the item to delete.",
          "$ref": "Location"
        }
      },
      "type": "object",
      "id": "DeleteItemRequest"
    },
##########################################################################################################################################################################################################
    "TextAnswer": {
      "description": "An answer to a question represented as text.",
      "properties": {
        "value": {
          "description": "Output only. The answer value. Formatting used for different kinds of question: * ChoiceQuestion * `RADIO` or `DROP_DOWN`: A single string corresponding to the option that was selected. * `CHECKBOX`: Multiple strings corresponding to each option that was selected. * TextQuestion: The text that the user entered. * ScaleQuestion: A string containing the number that was selected. * DateQuestion * Without time or year: MM-DD e.g. \"05-19\" * With year: YYYY-MM-DD e.g. \"1986-05-19\" * With time: MM-DD HH:MM e.g. \"05-19 14:51\" * With year and time: YYYY-MM-DD HH:MM e.g. \"1986-05-19 14:51\" * TimeQuestion: String with time or duration in HH:MM format e.g. \"14:51\" * RowQuestion within QuestionGroupItem: The answer for each row of a QuestionGroupItem is represented as a separate Answer. Each will contain one string for `RADIO`-type choices or multiple strings for `CHECKBOX` choices.",
          "type": "string",
          "readOnly": true
        }
      },
      "type": "object",
      "id": "TextAnswer"
    },
##########################################################################################################################################################################################################
    "FileUploadAnswers": {
      "type": "object",
      "properties": {
        "answers": {
          "type": "array",
          "items": {
            "$ref": "FileUploadAnswer"
          },
          "readOnly": true,
          "description": "Output only. All submitted files for a FileUpload question."
        }
      },
      "id": "FileUploadAnswers",
      "description": "All submitted files for a FileUpload question."
    },
##########################################################################################################################################################################################################
    "Feedback": {
      "description": "Feedback for a respondent about their response to a question.",
      "type": "object",
      "properties": {
        "material": {
          "type": "array",
          "items": {
            "$ref": "ExtraMaterial"
          },
          "description": "Additional information provided as part of the feedback, often used to point the respondent to more reading and resources."
        },
        "text": {
          "description": "Required. The main text of the feedback.",
          "type": "string"
        }
      },
      "id": "Feedback"
    }
  },
##########################################################################################################################################################################################################
  "icons": {
    "x32": "http://www.google.com/images/icons/product/search-32.gif",
    "x16": "http://www.google.com/images/icons/product/search-16.gif"
  },
##########################################################################################################################################################################################################
  "parameters": {
    "key": {
      "location": "query",
      "type": "string",
      "description": "API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token."
    },
##########################################################################################################################################################################################################
    "prettyPrint": {
      "location": "query",
      "type": "boolean",
      "description": "Returns response with indentations and line breaks.",
      "default": "true"
    },
##########################################################################################################################################################################################################
    "access_token": {
      "type": "string",
      "location": "query",
      "description": "OAuth access token."
    },
##########################################################################################################################################################################################################
    "fields": {
      "description": "Selector specifying which fields to include in a partial response.",
      "location": "query",
      "type": "string"
    },
##########################################################################################################################################################################################################
    "callback": {
      "type": "string",
      "location": "query",
      "description": "JSONP"
    },
##########################################################################################################################################################################################################
    "uploadType": {
      "type": "string",
      "description": "Legacy upload protocol for media (e.g. \"media\", \"multipart\").",
      "location": "query"
    },
##########################################################################################################################################################################################################
    "$.xgafv": {
      "enum": [
        "1",
        "2"
      ],
      "enumDescriptions": [
        "v1 error format",
        "v2 error format"
      ],
      "type": "string",
      "location": "query",
      "description": "V1 error format."
    },
##########################################################################################################################################################################################################
    "alt": {
      "location": "query",
      "description": "Data format for response.",
      "enumDescriptions": [
        "Responses with Content-Type of application/json",
        "Media download with context-dependent Content-Type",
        "Responses with Content-Type of application/x-protobuf"
      ],
      "default": "json",
      "enum": [
        "json",
        "media",
        "proto"
      ],
      "type": "string"
    },
##########################################################################################################################################################################################################
    "quotaUser": {
      "location": "query",
      "description": "Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.",
      "type": "string"
    },
##########################################################################################################################################################################################################
    "upload_protocol": {
      "description": "Upload protocol for media (e.g. \"raw\", \"multipart\").",
      "location": "query",
      "type": "string"
    },
##########################################################################################################################################################################################################
    "oauth_token": {
      "type": "string",
      "description": "OAuth 2.0 token for the current user.",
      "location": "query"
    }
  },
##########################################################################################################################################################################################################
  "version": "v1",
  "ownerName": "Google",
  "basePath": "",
  "auth": {
    "oauth2": {
      "scopes": {
        "https://www.googleapis.com/auth/drive": {
          "description": "See, edit, create, and delete all of your Google Drive files"
        },
        "https://www.googleapis.com/auth/drive.readonly": {
          "description": "See and download all your Google Drive files"
        },
        "https://www.googleapis.com/auth/drive.file": {
          "description": "See, edit, create, and delete only the specific Google Drive files you use with this app"
        }
      }
    }
  },
##########################################################################################################################################################################################################
  "version_module": true,
  "protocol": "rest",
  "revision": "20220322",
  "name": "forms",
  "canonicalName": "Forms",
  "rootUrl": "https://forms.googleapis.com/",
  "title": "Google Forms API",
  "fullyEncodeReservedExpansion": true,
  "batchPath": "batch",
  "description": "Reads and writes Google Forms and responses.",
  "resources": {
    "forms": {
      "resources": {
        "watches": {
          "methods": {
            "delete": {
              "parameters": {
                "watchId": {
                  "type": "string",
                  "description": "Required. The ID of the Watch to delete.",
                  "required": true,
                  "location": "path"
                },
                "formId": {
                  "required": true,
                  "location": "path",
                  "description": "Required. The ID of the Form.",
                  "type": "string"
                }
              },
              "flatPath": "v1/forms/{formId}/watches/{watchId}",
              "response": {
                "$ref": "Empty"
              },
              "id": "forms.forms.watches.delete",
              "httpMethod": "DELETE",
              "parameterOrder": [
                "formId",
                "watchId"
              ],
              "scopes": [
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive.readonly"
              ],
              "path": "v1/forms/{formId}/watches/{watchId}",
              "description": "Delete a watch."
            },
##########################################################################################################################################################################################################
            "renew": {
              "scopes": [
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive.readonly"
              ],
              "parameters": {
                "formId": {
                  "location": "path",
                  "description": "Required. The ID of the Form.",
                  "type": "string",
                  "required": true
                },
                "watchId": {
                  "location": "path",
                  "type": "string",
                  "required": true,
                  "description": "Required. The ID of the Watch to renew."
                }
              },
              "response": {
                "$ref": "Watch"
              },
              "flatPath": "v1/forms/{formId}/watches/{watchId}:renew",
              "id": "forms.forms.watches.renew",
              "description": "Renew an existing watch for seven days. The state of the watch after renewal is `ACTIVE`, and the `expire_time` is seven days from the renewal. Renewing a watch in an error state (e.g. `SUSPENDED`) succeeds if the error is no longer present, but fail otherwise. After a watch has expired, RenewWatch returns `NOT_FOUND`.",
              "request": {
                "$ref": "RenewWatchRequest"
              },
              "path": "v1/forms/{formId}/watches/{watchId}:renew",
              "parameterOrder": [
                "formId",
                "watchId"
              ],
              "httpMethod": "POST"
            },
##########################################################################################################################################################################################################
            "create": {
              "request": {
                "$ref": "CreateWatchRequest"
              },
              "parameters": {
                "formId": {
                  "description": "Required. ID of the Form to watch.",
                  "type": "string",
                  "required": true,
                  "location": "path"
                }
              },
              "parameterOrder": [
                "formId"
              ],
              "flatPath": "v1/forms/{formId}/watches",
              "description": "Create a new watch. If a watch ID is provided, it must be unused. For each invoking project, the per form limit is one watch per Watch.EventType. A watch expires seven days after it is created (see Watch.expire_time).",
              "id": "forms.forms.watches.create",
              "httpMethod": "POST",
              "scopes": [
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive.readonly"
              ],
              "response": {
                "$ref": "Watch"
              },
              "path": "v1/forms/{formId}/watches"
            },
##########################################################################################################################################################################################################
            "list": {
              "description": "Return a list of the watches owned by the invoking project. The maximum number of watches is two: For each invoker, the limit is one for each event type per form.",
              "id": "forms.forms.watches.list",
              "path": "v1/forms/{formId}/watches",
              "scopes": [
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/drive.file",
                "https://www.googleapis.com/auth/drive.readonly"
              ],
              "parameters": {
                "formId": {
                  "location": "path",
                  "type": "string",
                  "description": "Required. ID of the Form whose watches to list.",
                  "required": true
                }
              },
              "flatPath": "v1/forms/{formId}/watches",
              "httpMethod": "GET",
              "response": {
                "$ref": "ListWatchesResponse"
              },
              "parameterOrder": [
                "formId"
              ]
            }
          }
        },
##########################################################################################################################################################################################################
        "responses": {
          "methods": {
            "list": {
              "flatPath": "v1/forms/{formId}/responses",
              "httpMethod": "GET",
              "id": "forms.forms.responses.list",
              "path": "v1/forms/{formId}/responses",
              "scopes": [
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/drive.file"
              ],
              "parameterOrder": [
                "formId"
              ],
              "response": {
                "$ref": "ListFormResponsesResponse"
              },
              "parameters": {
                "formId": {
                  "location": "path",
                  "description": "Required. ID of the Form whose responses to list.",
                  "type": "string",
                  "required": true
                },
                "pageToken": {
                  "location": "query",
                  "description": "A page token returned by a previous list response. If this field is set, the form and the values of the filter must be the same as for the original request.",
                  "type": "string"
                },
                "pageSize": {
                  "description": "The maximum number of responses to return. The service may return fewer than this value. If unspecified or zero, at most 5000 responses are returned.",
                  "location": "query",
                  "type": "integer",
                  "format": "int32"
                },
                "filter": {
                  "type": "string",
                  "location": "query",
                  "description": "Which form responses to return. Currently, the only supported filters are: * timestamp \u003e *N* which means to get all form responses submitted after (but not at) timestamp *N*. * timestamp \u003e= *N* which means to get all form responses submitted at and after timestamp *N*. For both supported filters, timestamp must be formatted in RFC3339 UTC \"Zulu\" format. Examples: \"2014-10-02T15:01:23Z\" and \"2014-10-02T15:01:23.045123456Z\"."
                }
              },
              "description": "List a form's responses."
            },
##########################################################################################################################################################################################################
            "get": {
              "parameterOrder": [
                "formId",
                "responseId"
              ],
              "flatPath": "v1/forms/{formId}/responses/{responseId}",
              "description": "Get one response from the form.",
              "path": "v1/forms/{formId}/responses/{responseId}",
              "httpMethod": "GET",
              "parameters": {
                "responseId": {
                  "description": "Required. The response ID within the form.",
                  "required": true,
                  "type": "string",
                  "location": "path"
                },
                "formId": {
                  "required": true,
                  "type": "string",
                  "location": "path",
                  "description": "Required. The form ID."
                }
              },
              "id": "forms.forms.responses.get",
              "scopes": [
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/drive.file"
              ],
              "response": {
                "$ref": "FormResponse"
              }
            }
          }
        }
      },
##########################################################################################################################################################################################################
      "methods": {
        "get": {
          "parameters": {
            "formId": {
              "type": "string",
              "description": "Required. The form ID.",
              "location": "path",
              "required": true
            }
          },
          "httpMethod": "GET",
          "description": "Get a form.",
          "path": "v1/forms/{formId}",
          "scopes": [
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive.readonly"
          ],
          "id": "forms.forms.get",
          "flatPath": "v1/forms/{formId}",
          "response": {
            "$ref": "Form"
          },
          "parameterOrder": [
            "formId"
          ]
        },
##########################################################################################################################################################################################################
        "create": {
          "description": "Create a new form using the title given in the provided form message in the request. *Important:* Only the form.info.title and form.info.document_title fields are copied to the new form. All other fields including the form description, items and settings are disallowed. To create a new form and add items, you must first call forms.create to create an empty form with a title and (optional) document title, and then call forms.update to add the items.",
          "parameters": {},
          "id": "forms.forms.create",
          "scopes": [
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/drive.file"
          ],
          "httpMethod": "POST",
          "path": "v1/forms",
          "flatPath": "v1/forms",
          "parameterOrder": [],
          "request": {
            "$ref": "Form"
          },
          "response": {
            "$ref": "Form"
          }
        },
##########################################################################################################################################################################################################
        "batchUpdate": {
          "id": "forms.forms.batchUpdate",
          "parameters": {
            "formId": {
              "description": "Required. The form ID.",
              "location": "path",
              "type": "string",
              "required": true
            }
          },
##########################################################################################################################################################################################################
          "response": {
            "$ref": "BatchUpdateFormResponse"
          },
##########################################################################################################################################################################################################
          "description": "Change the form with a batch of updates.",
          "parameterOrder": [
            "formId"
          ],
##########################################################################################################################################################################################################
          "scopes": [
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/drive.file"
          ],
##########################################################################################################################################################################################################
          "path": "v1/forms/{formId}:batchUpdate",
          "flatPath": "v1/forms/{formId}:batchUpdate",
          "httpMethod": "POST",
          "request": {
            "$ref": "BatchUpdateFormRequest"
          }
        }
      }
    }
  },
  "ownerDomain": "google.com",
  "baseUrl": "https://forms.googleapis.com/",
  "discoveryVersion": "v1",
  "kind": "discovery#restDescription"
}
