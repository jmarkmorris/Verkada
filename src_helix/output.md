================================================================================
 Running Verkada API Automated Tests
 Log Level: INFO
================================================================================

--------------------------------------------------------------------------------
Running Test: Get API Token
Script: test_token_api.py
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Running: python -m src_helix.test_token_api --log_level INFO 
--------------------------------------------------------------------------------
2025-04-26 22:13:48,023 - __main__ - INFO - Successfully retrieved API token: v2_b3c5d9a...

--- Token API Response ---
{
    "token": "v2_b3c5d9a59a6d12cbef2110b2e1f4ec2d"
}
2025-04-26 22:13:48,024 - src_helix.api_utils - INFO - Generated JSON template: src_helix/api-json/test_token_api.json
PASS: Get API Token

--------------------------------------------------------------------------------
Running Test: Access Users List
Script: test_users_list_api.py
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Running: python -m src_helix.test_users_list_api --log_level INFO 
--------------------------------------------------------------------------------

--- Access Users List API Response ---
{
    "access_members": [
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cabinet Install Michael Danino Arleen Lively",
            "has_profile_photo": false,
            "user_id": "00439f7b-74ac-4a3f-b0f2-5e6500fae55f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Scott Swaringen Jeff Johnston",
            "has_profile_photo": false,
            "user_id": "010d436b-53e4-4e53-9c39-fa9b8b5a8092"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mitch McAfee Construction Arleen Lively",
            "has_profile_photo": false,
            "user_id": "011e7191-7b3a-4dcf-b7c5-999fd61d85e4"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mary Pancner",
            "has_profile_photo": false,
            "user_id": "01edec6f-fcbc-4451-ba9c-e0252b8acfa3"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sotero Garcia Gardener Jennie Concannon",
            "has_profile_photo": false,
            "user_id": "0276a9c5-2864-441e-a5a3-9ee5a3524b01"
        },
        {
            "email": "refornaca81@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rachel Fornaca",
            "has_profile_photo": false,
            "user_id": "0279f249-dd4f-46ba-a8fe-4750e8a7e090"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Garbriel Pat Tanabe",
            "has_profile_photo": false,
            "user_id": "0292ba72-7c19-45a5-97e7-c003b7da34dd"
        },
        {
            "email": "listings@shafranrealty.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Brenna Harper",
            "has_profile_photo": false,
            "user_id": "040a9220-3f0c-4b56-bc96-ba54960bd286"
        },
        {
            "email": "robertlagge@ferrellgas.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ferrellgas Colleen Lister",
            "has_profile_photo": false,
            "user_id": "0477c48e-ad83-416c-8d76-8e1fac2db553"
        },
        {
            "email": "spectrumplumbing@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Dave Greaves",
            "has_profile_photo": false,
            "user_id": "048041ff-9d15-4459-9e47-ef0fb935f4a4"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Julia Rolon",
            "has_profile_photo": false,
            "user_id": "04cad6e1-2825-426f-8c1a-f84cee952b56"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rosy Baza caregiver Byung Kang",
            "has_profile_photo": false,
            "user_id": "050de4c3-0542-4ebe-a6a8-f1af50e00589"
        },
        {
            "email": "cyberflugo@me.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Fernando Lugo",
            "has_profile_photo": false,
            "user_id": "05957fd9-0c17-4828-8347-050e941a5c9f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Marcia Palmer",
            "has_profile_photo": false,
            "user_id": "064c9578-36b6-4ec1-a9f3-82c108b8234d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "MGWW 29460 Dannielle Milliken",
            "has_profile_photo": false,
            "user_id": "07e18220-b3f9-4865-91f3-f65aa6a2821e"
        },
        {
            "email": "twm139@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Terrence Martin",
            "has_profile_photo": false,
            "user_id": "081cce00-cc15-4dbc-b97d-968f92bed3ac"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Diana Villalobos",
            "has_profile_photo": false,
            "user_id": "086ee431-31d4-48c3-b992-accb0334c838"
        },
        {
            "email": "jaimeramirez59@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jaime Ramirez",
            "has_profile_photo": false,
            "user_id": "0895cbd2-ab57-4b3b-8b17-7a768ca996fa"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "SanTizelT LLC Kelley Scutelnicu",
            "has_profile_photo": false,
            "user_id": "089f9e5f-f181-4877-a6ee-f50d108de498"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pablo Matias gardener Melanie Thompson",
            "has_profile_photo": false,
            "user_id": "09233f42-f946-471a-8c56-efc9b353f772"
        },
        {
            "email": "kimydebow@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kim DeBow",
            "has_profile_photo": false,
            "user_id": "097de7ef-b8ca-4550-bf4f-b12e9f2288fb"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock 11/11/23 once Heavens",
            "has_profile_photo": false,
            "user_id": "0999081a-ac49-4094-ac05-a3691a8fc76c"
        },
        {
            "email": "support+marcwrona+1723578315@verkada.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Verkada Support",
            "has_profile_photo": false,
            "user_id": "0b06d397-4ed8-4a01-8af7-2f5d1428a0b2"
        },
        {
            "email": "michaelrfranklin@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Michael Franklin",
            "has_profile_photo": false,
            "user_id": "0b79c82a-ea43-4fdc-af50-7c670c81928e"
        },
        {
            "email": "yunashin@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Yuna Shin",
            "has_profile_photo": false,
            "user_id": "0b83ea92-2651-4215-99fa-09a1708b8fd6"
        },
        {
            "email": "mstepien1@cox.net",
            "employee_id": "",
            "external_id": "",
            "full_name": "Michael Stepien",
            "has_profile_photo": false,
            "user_id": "0c2d8ce8-1de1-45e6-b70b-c56c5842f280"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ramon Rascon Malacara Drywall Arleen Lively",
            "has_profile_photo": false,
            "user_id": "0c900106-f47e-4296-bb46-9639cbd6bf2d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "WHD 29052 Tanabe Zlotnicki",
            "has_profile_photo": false,
            "user_id": "0d6d22dc-a5f6-4f0f-b72d-484d4622d544"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Martin (8EUS532) Wronski",
            "has_profile_photo": false,
            "user_id": "0d71df0e-a9fe-4d5b-b43f-bc8b13dded6f"
        },
        {
            "email": "sobhhala387@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Hala Sobh",
            "has_profile_photo": false,
            "user_id": "0df68733-45d1-4370-8fbe-b2b78fd166ce"
        },
        {
            "email": "marsham760@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Marsha Michael",
            "has_profile_photo": false,
            "user_id": "0e239001-88ce-4a59-bf4a-a0bcd723efc8"
        },
        {
            "email": "delaneytojino@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Delaney Tojino",
            "has_profile_photo": false,
            "user_id": "0e3351a2-8aab-4dfe-af1b-a136fbcf7f97"
        },
        {
            "email": "antonia.aa@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Antonia Toupet",
            "has_profile_photo": false,
            "user_id": "0f8e7cb9-f888-4824-b48f-2d83e88b08e6"
        },
        {
            "email": "geoffree@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Daston Bagheri",
            "has_profile_photo": false,
            "user_id": "100df4e9-f325-4fc1-a49d-3363df5c6524"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Katie Concannon",
            "has_profile_photo": false,
            "user_id": "10282b33-9ca9-4fdd-b189-733d087b9ef4"
        },
        {
            "email": "lia@lmcassets.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Lia Flynn",
            "has_profile_photo": false,
            "user_id": "10e54456-5fe4-4bb1-b599-282dbf74586c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sam Yoon",
            "has_profile_photo": false,
            "user_id": "11d222a3-50e9-4720-9ac8-2f80f068190d"
        },
        {
            "email": "jrsidhwa@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jacquelyn Sidhwa",
            "has_profile_photo": false,
            "user_id": "12082f40-4f4d-4d52-9324-90c2ef5e7b36"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Aimara Fernandez",
            "has_profile_photo": false,
            "user_id": "124137d2-128f-4544-903b-87be77ac2df7"
        },
        {
            "email": "jon.fagerstrom@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jon Fagerstrom",
            "has_profile_photo": false,
            "user_id": "126b15dc-949a-4023-ab4f-2057e2b4aa05"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ed Ochoa",
            "has_profile_photo": false,
            "user_id": "127ebbe7-f190-40bc-8fc8-8aa78476513e"
        },
        {
            "email": "alohahelen@aol.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Helen Wallace",
            "has_profile_photo": false,
            "user_id": "12ceb19c-2e1a-46b2-9e4d-d604bf6f7917"
        },
        {
            "email": "alyssa.rolle93@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Steve & Alyssa Rolle",
            "has_profile_photo": false,
            "user_id": "13835857-5472-4f13-a5de-df5b1ede5e4f"
        },
        {
            "email": "beedaniel16@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Brook Daniel Husband",
            "has_profile_photo": false,
            "user_id": "15803619-63d3-4166-b1de-2fdd5b247516"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jihan Abdulhalim",
            "has_profile_photo": false,
            "user_id": "16604ede-35f9-4476-82a3-2e772ad9b0e8"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sharon Cook",
            "has_profile_photo": false,
            "user_id": "167efdf6-cd1a-4861-89c6-320e52eadce4"
        },
        {
            "email": "jborg760@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Joel Borg",
            "has_profile_photo": false,
            "user_id": "176b4f9a-448b-4895-bc1f-d48ffb92a7ad"
        },
        {
            "email": "mark@noserf.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mark Opaskar",
            "has_profile_photo": false,
            "user_id": "17a55a52-ba6c-4862-9346-bdade203c111"
        },
        {
            "email": "dawnkorinek@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Dawn Fuller",
            "has_profile_photo": false,
            "user_id": "17bdfcdb-05ff-4387-97cf-4cc8e1dafe42"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "son Errez",
            "has_profile_photo": false,
            "user_id": "17fa2f47-6a0e-4b0e-9473-8e090167c373"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Keycard used by Ben Errez",
            "has_profile_photo": false,
            "user_id": "18127fe3-c9a5-49f2-9b08-39e3f0fc5530"
        },
        {
            "email": "zippy.smile01@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Yoke Ho",
            "has_profile_photo": false,
            "user_id": "18b0366c-ae38-40d0-a57d-7ed2750810cd"
        },
        {
            "email": "jenpaxton@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jennifer Paxton",
            "has_profile_photo": false,
            "user_id": "18e10ce1-4e18-407b-bab0-f0397678df17"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Dave Hofer Home Front Ent. Arleen  Lively",
            "has_profile_photo": false,
            "user_id": "19097201-5441-41c7-835e-ce8e66ff8916"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Chris Concannon",
            "has_profile_photo": false,
            "user_id": "1921a349-ecbe-4253-afb8-b8e7deac90de"
        },
        {
            "email": "stuoster39@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Stu Oster",
            "has_profile_photo": false,
            "user_id": "19370478-47eb-44be-9cd3-4cbbffd8b483"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ruben Cruz Gardener Jeff Johnston",
            "has_profile_photo": false,
            "user_id": "1981bca8-d8a8-4006-9c16-f89bc421ab41"
        },
        {
            "email": "madelynbasinet@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Madelyn Basinet",
            "has_profile_photo": false,
            "user_id": "1aa412a5-44fa-4714-9e3e-2ac8dad9ed9e"
        },
        {
            "email": "Berrez@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ben GF Errez",
            "has_profile_photo": false,
            "user_id": "1b800fc9-7a98-44de-b9db-a61894d468ab"
        },
        {
            "email": "marie.kempka@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Marie Kempka",
            "has_profile_photo": false,
            "user_id": "1bcd95e7-5f5b-4519-80ee-0524114a8aa1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mark Gregson Lot 64",
            "has_profile_photo": false,
            "user_id": "1c00f3a9-da75-4a2d-877b-aa4de5e7f333"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Feriba Albarran",
            "has_profile_photo": false,
            "user_id": "1c2b3f3a-1980-4fdf-8ddb-51be50b4dc9e"
        },
        {
            "email": "sandymillisonbc@frontier.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sandy Honz",
            "has_profile_photo": false,
            "user_id": "1c7984e7-6877-4d80-89ee-d3cdeb9d357a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Josefa Lorenzo Cleaning Dawn Korink",
            "has_profile_photo": false,
            "user_id": "1d498b4c-7f0a-44f0-b68b-2060a962c6df"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Bob Stall Community Glass Arleen Lively",
            "has_profile_photo": false,
            "user_id": "1d75ba1b-4ef0-4ff1-9d4a-018ef2134f5d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kenna Payne",
            "has_profile_photo": false,
            "user_id": "1dbce0c3-9d8b-481d-bd25-f1a5bc56d268"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Romero Paint Omar Orozco Arleen Lively",
            "has_profile_photo": false,
            "user_id": "1dcb3075-9423-445d-aa4d-4645b54a577c"
        },
        {
            "email": "kimcrn@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kim Colonnelli",
            "has_profile_photo": false,
            "user_id": "1f36ab81-d268-45cf-9bce-cd1d1d8c2e69"
        },
        {
            "email": "rleesd@outlook.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Robert Hunt",
            "has_profile_photo": false,
            "user_id": "1f9fbba2-ffb4-46ac-a517-3244f757dfe3"
        },
        {
            "email": "isaisilva11@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Izzy Silva caretaker Kang",
            "has_profile_photo": false,
            "user_id": "1ffd8f0b-93e7-47a7-80b4-23dcfa8d40cf"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gardner Anthony Siaweleski",
            "has_profile_photo": false,
            "user_id": "202717c8-9077-4fd8-9785-7b94f2b76fcf"
        },
        {
            "email": "mvillariasa@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mackenzie Villariasa",
            "has_profile_photo": false,
            "user_id": "20418b54-98b3-48af-b091-fb64ca72dc79"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Augie handyman Mary Kate Lowe",
            "has_profile_photo": false,
            "user_id": "20b6e787-eaf9-490b-a458-068019fd715a"
        },
        {
            "email": "montemurodesign@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Michael (Mickey) Montemuro",
            "has_profile_photo": false,
            "user_id": "217e8f84-48b5-4ae9-bfd3-73e9edcd0009"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "David Korinek",
            "has_profile_photo": false,
            "user_id": "22620da7-7f42-44c9-8636-733a28eb127a"
        },
        {
            "email": "edward.barak@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Edward Barak",
            "has_profile_photo": false,
            "user_id": "22860c6e-708d-4ce9-9053-a739eb96bb30"
        },
        {
            "email": "rengel16@me.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rebecca Zarza",
            "has_profile_photo": false,
            "user_id": "22bed484-da40-4ba0-9812-04945c38056f"
        },
        {
            "email": "jillwhan@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jill Whan",
            "has_profile_photo": false,
            "user_id": "22d8a89a-1d75-46fc-8cc5-ec3ae46993b2"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "David Hanlon",
            "has_profile_photo": false,
            "user_id": "2342657f-7e8c-4675-a6dd-b8ddbb7508df"
        },
        {
            "email": "mgsilveira1@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "50 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "23811a6a-b997-4336-8b32-fb58aa63fcef"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jabier Torres Arleen Lively",
            "has_profile_photo": false,
            "user_id": "23ac0a4f-f737-4a9d-a855-2381a0506ebc"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ivan house cleaning Rosa Gonzalez",
            "has_profile_photo": false,
            "user_id": "2522f7e9-3140-4502-beb8-9099df440065"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "JC Landscapping Furgerson",
            "has_profile_photo": false,
            "user_id": "25918bfc-1ed2-4fc6-9d89-d4351daea092"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Luke Hunt",
            "has_profile_photo": false,
            "user_id": "25dc9fcb-a2bc-41ff-a536-0c38e7117f20"
        },
        {
            "email": "dandankiannasr@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "93 Welk Highland Drive",
            "has_profile_photo": false,
            "user_id": "25dd9ef3-5458-4ea8-b5d7-d4b252c9aae9"
        },
        {
            "email": "pat.tanabe@3zconsulting.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pat Tanabe",
            "has_profile_photo": false,
            "user_id": "26aa16cc-4fbf-4a0f-b7a8-c65d2108dfbf"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Glenn Shaw",
            "has_profile_photo": false,
            "user_id": "26c90c85-01b5-4a1b-8769-673080f94018"
        },
        {
            "email": "sc1cook2@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sharon Lot 34 Cook no LP",
            "has_profile_photo": false,
            "user_id": "270888cd-ca07-4522-b995-981fc357cdc7"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pool cleaning Natasha Bailey Sawh",
            "has_profile_photo": false,
            "user_id": "27873510-ddc5-4720-ad83-f1a6ee9ac3a1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Maricela Cleaning Service Adam Levy",
            "has_profile_photo": false,
            "user_id": "27e451f1-b797-4c1e-943b-6acfb5467d9d"
        },
        {
            "email": "jakeluis93@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jake Luis",
            "has_profile_photo": false,
            "user_id": "27efdb22-7b56-4f37-8661-6a1785a95292"
        },
        {
            "email": "pat.tanabe@3zconsultimg.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pat tanabe",
            "has_profile_photo": false,
            "user_id": "27f25ca5-41e3-4364-ab18-92947428e1c1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "CertaPro Manuel Vargas Carrie Hartwick",
            "has_profile_photo": false,
            "user_id": "288af9be-1dca-4e1f-871e-b1e54206ed26"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Valley Center Water District",
            "has_profile_photo": false,
            "user_id": "2922030e-8ae0-4c39-902f-feecb2ed225a"
        },
        {
            "email": "jbestmartin@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jennifer Best-Martin",
            "has_profile_photo": false,
            "user_id": "292533ea-d796-4850-9704-3a0aed279343"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Noel Johnson",
            "has_profile_photo": false,
            "user_id": "29adfd11-e35d-463a-b6a4-25d77c7d9eed"
        },
        {
            "email": "l.bravo3@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Leonardo Bravo",
            "has_profile_photo": false,
            "user_id": "29e94d36-f496-4e54-a088-14224ca5ff1b"
        },
        {
            "email": "adamlevy11@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Adam Levy",
            "has_profile_photo": false,
            "user_id": "29f43df4-676d-4ab7-a4c5-545a858b596a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pool Wizard Pool & Spa Furgerson",
            "has_profile_photo": false,
            "user_id": "2a68f4c4-5507-4dd6-8337-05da1c849d06"
        },
        {
            "email": "jcdemeules@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jeanne DeMeules",
            "has_profile_photo": false,
            "user_id": "2aa1de28-c785-49ae-a296-68c0eb8ff9e5"
        },
        {
            "email": "kathleendelmastro3@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kathleen Delmastro",
            "has_profile_photo": false,
            "user_id": "2b300b90-cbba-47ea-80ef-ca69a62d7bca"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mykhailo Mykhailov",
            "has_profile_photo": false,
            "user_id": "2bbf451e-96e9-4201-8e49-ee72e41aeab1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Antonio Ramero Paint Arleen Lively",
            "has_profile_photo": false,
            "user_id": "2ccd94cc-88e4-47bc-9fb8-0c77641d44ee"
        },
        {
            "email": "morebetterllc@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Hal Bassett",
            "has_profile_photo": false,
            "user_id": "2d1c8fb6-1d0f-4f5c-b1ce-d27485d5e51b"
        },
        {
            "email": "chris@vintagecellars.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Christopher Noel",
            "has_profile_photo": false,
            "user_id": "2d34ed50-ac75-4c35-8804-5650db2dd276"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Fred Clark CRC Engineering",
            "has_profile_photo": false,
            "user_id": "2d59102f-f06c-418d-bfa7-7e71e3ee9c4d"
        },
        {
            "email": "gregsonm@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mark Gregson",
            "has_profile_photo": false,
            "user_id": "2daac6c2-305d-40c7-a60e-50a0eacf5e8e"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mark Gregson Lot 65",
            "has_profile_photo": false,
            "user_id": "2dea02ad-3365-4c5a-906a-d68a3d9f4f2b"
        },
        {
            "email": "carmen.multhauf@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Carmen Multhauf",
            "has_profile_photo": false,
            "user_id": "2dfa1718-4630-4491-a114-b767c775c5c2"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ramon Duran BVI Solar Arleen Lively",
            "has_profile_photo": false,
            "user_id": "2e239313-947a-4c2c-9768-1638947ea44a"
        },
        {
            "email": "Tyler.Scutelnicu@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Tyler Scutelnicu",
            "has_profile_photo": false,
            "user_id": "2e6b2170-8037-4d7e-b1a9-15f9ea952222"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gardener Tom Graves",
            "has_profile_photo": false,
            "user_id": "2f14a4b6-ddac-4968-ae8b-2c3d249cc6ae"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Joseph Hernandaz",
            "has_profile_photo": false,
            "user_id": "2f1d8d4d-a1e4-4df0-b8a7-4bcc8ed38f30"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Exterminator Ben Errez",
            "has_profile_photo": false,
            "user_id": "2f6f90b3-027e-47e8-8072-b47948c644ac"
        },
        {
            "email": "clearblueeric@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Eric Rumbin Vinny Lostetter",
            "has_profile_photo": false,
            "user_id": "2fc4a54e-072a-4e45-898f-7dee3a0cae30"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ja Nielle Karla Hernandaz",
            "has_profile_photo": false,
            "user_id": "305d8d1e-0cbb-44c0-8656-6690b13fe8bf"
        },
        {
            "email": "sateesharjula@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sateesh Arjula",
            "has_profile_photo": false,
            "user_id": "306176d6-4fd8-417b-b726-43336296337b"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pat Frazier",
            "has_profile_photo": false,
            "user_id": "30a04d59-79de-437f-92ac-c14194ac4f1a"
        },
        {
            "email": "USLuxhome01@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mary Kate Lowe Rental agent",
            "has_profile_photo": false,
            "user_id": "30a56dc9-c7a2-43a9-b31b-9d4b990f93b7"
        },
        {
            "email": "ez_molla@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Zainab Ellen Molla",
            "has_profile_photo": false,
            "user_id": "30e1bdd3-76ce-4ff6-a420-6e91e215f963"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Tarah Djobo dog sitter Steve Hermosillo",
            "has_profile_photo": false,
            "user_id": "30e9ad7b-fd89-47d5-b5ff-53898ebcfcb5"
        },
        {
            "email": "jreyes84@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "26 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "31601acf-b660-4f2a-a18e-7fa87c8c7423"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Theron Frazier",
            "has_profile_photo": false,
            "user_id": "318edb87-8656-4539-98fc-59d6dc3d30f0"
        },
        {
            "email": "lostfamily@me.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Adrienne Lostetter",
            "has_profile_photo": false,
            "user_id": "328a33cd-f489-4ac2-83c1-08cdae715d8e"
        },
        {
            "email": "vjs@sabresciences.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "27 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "331f867f-4d47-4c05-9165-f544211a4f47"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jesus Avalos contractor Martin Wronski",
            "has_profile_photo": false,
            "user_id": "33d5a2b6-e5d9-4e60-a11a-1e6c1c62a4f4"
        },
        {
            "email": "crgrant62@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Chris Grant",
            "has_profile_photo": false,
            "user_id": "351f3faa-3c60-42b1-95f7-742038fe7d0a"
        },
        {
            "email": "kfurgerson85@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kyle Furgerson",
            "has_profile_photo": false,
            "user_id": "3531fad6-1a75-4f0b-9db5-77b752d322c6"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Clear Expectations Pool Karla Hernandaz",
            "has_profile_photo": false,
            "user_id": "3548bdba-cee7-474e-930e-1d5b04ebd878"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Luis Lifetime Custom Painting Alejandra Cadena Perez",
            "has_profile_photo": false,
            "user_id": "35a7e9c0-4c47-4519-b704-2a32e5b023a7"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "LCL9778 Dawn Korinek",
            "has_profile_photo": false,
            "user_id": "366a6e43-e53c-4457-9499-edceaeaafdf7"
        },
        {
            "email": "jim.korinek@cbre.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jim Korinek",
            "has_profile_photo": false,
            "user_id": "36e56cf1-f4bf-4a85-aee1-133e97879cff"
        },
        {
            "email": "Arielsbergstrom@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ariel Bergstrom",
            "has_profile_photo": false,
            "user_id": "36f989ba-831d-42ab-9d57-c1a227a62664"
        },
        {
            "email": "jdavitt22@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Joey Davitt",
            "has_profile_photo": false,
            "user_id": "375e20ba-a74f-46e7-ae1e-f08e030e096e"
        },
        {
            "email": "cccpoolservicesinc@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "CCC Pool Hartwick",
            "has_profile_photo": false,
            "user_id": "377f7535-cd44-42a9-b110-eecc2bc3375c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "James Thompson",
            "has_profile_photo": false,
            "user_id": "37d9d14c-3bbd-4507-a1ff-7878c984a181"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Diana Rehagen",
            "has_profile_photo": false,
            "user_id": "37e418b5-0db0-414a-a727-da58422f701f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock Heavens",
            "has_profile_photo": false,
            "user_id": "38fc65e4-5028-43bb-a24f-e524be7c6e7e"
        },
        {
            "email": "basinet@aol.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Michael Basinet",
            "has_profile_photo": false,
            "user_id": "3982769c-4a79-431a-8ef6-925a2d5612c2"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mark Gregson Lot 66",
            "has_profile_photo": false,
            "user_id": "3a4492d0-2bf5-4f51-9feb-e5bee7b0c11b"
        },
        {
            "email": "peter.minkoff@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Peter Minkoff",
            "has_profile_photo": false,
            "user_id": "3a576a29-0a22-4577-bd11-2f16703413ea"
        },
        {
            "email": "nlostetter99@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Nicholas Lostetter",
            "has_profile_photo": false,
            "user_id": "3a593f3f-ad0c-4f49-b33c-4ad9f0220757"
        },
        {
            "email": "csquinteromd63@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Carolyn Quintero",
            "has_profile_photo": false,
            "user_id": "3a725a22-5533-4394-9012-fa152d62e1b6"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jose Cruz Landscapers Sheri Basinet",
            "has_profile_photo": false,
            "user_id": "3a8293a8-e277-4084-8569-4570c3fee578"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jason Simple Pest Control Mary Kate Lowe",
            "has_profile_photo": false,
            "user_id": "3ab207aa-a2d5-44ae-b744-c54fe493417e"
        },
        {
            "email": "dvf436@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "David Fernandez",
            "has_profile_photo": false,
            "user_id": "3ac9a59f-9868-470c-845b-51d13551c63c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "CertaPro Pablo Martinez Carrie Hartwick",
            "has_profile_photo": false,
            "user_id": "3b072d64-acaa-422e-a169-fe79ae20b66b"
        },
        {
            "email": "sdsree02@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sowmya Patibandla",
            "has_profile_photo": false,
            "user_id": "3b40b17e-3678-404d-b7e6-06eaab26ae1b"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Artemio Vasquez Gardener Peter Minkoff",
            "has_profile_photo": false,
            "user_id": "3b5e7d81-12ec-415b-aa44-c85afda46cbf"
        },
        {
            "email": "erinsunseri@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Erin Sunseri",
            "has_profile_photo": false,
            "user_id": "3b6c4cf2-860d-4eb4-a8df-3ac9ca3042b8"
        },
        {
            "email": "angelnat77@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Nataliya Chung",
            "has_profile_photo": false,
            "user_id": "3ba686c0-cee2-4368-bbfc-53662405128a"
        },
        {
            "email": "irynaozkan28@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Iryna Ozkan",
            "has_profile_photo": false,
            "user_id": "3bb7fcd4-4b24-4fef-9389-e8b41b1ba9c9"
        },
        {
            "email": "sam@vantedgeplans.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Hussam Elfarra",
            "has_profile_photo": false,
            "user_id": "3bdb3c3b-f6fe-4dc5-a307-1775e09489dd"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "50 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "3bfdd4ae-bdea-444e-9bc7-5d96fb84e298"
        },
        {
            "email": "calma2075@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Alma Rangel",
            "has_profile_photo": false,
            "user_id": "3c53e4d9-b2ae-4ab8-8fe2-3e3d54d43118"
        },
        {
            "email": "colleen@listerconstruction.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Colleen Lister",
            "has_profile_photo": false,
            "user_id": "3cb526e3-e85b-46d6-bbef-3a6e5a46019b"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Venancia Venegas Vinny Lostetter",
            "has_profile_photo": false,
            "user_id": "3cb6fd57-db8d-45da-b537-ffaad2022b8a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ray Dorame Former Master Craft Builder",
            "has_profile_photo": false,
            "user_id": "3cb76308-c7ab-47a9-8fca-0a27a7f70633"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Martin Salinas McAfee Construction Arleen Lively",
            "has_profile_photo": false,
            "user_id": "3d701ce5-f62f-4285-b49c-8cd8ebef446d"
        },
        {
            "email": "pcronkhite@edcodisposal.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "EdCo Disposal Paul Cronkhite",
            "has_profile_photo": false,
            "user_id": "3e38bc72-aa1c-4a30-b85b-8e1f4c6f565b"
        },
        {
            "email": "inspector@aboutcis.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kent Schafer",
            "has_profile_photo": false,
            "user_id": "3eaac69f-d7a9-4c17-af2e-f6ac183e29fa"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cesar Gonzalez",
            "has_profile_photo": false,
            "user_id": "3eae8eaa-6584-47bf-8ba2-7289718203a8"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "exterminator Ben Errez",
            "has_profile_photo": false,
            "user_id": "3eb30f56-0e56-47da-8266-1c527ca059dd"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Vadin Suh",
            "has_profile_photo": false,
            "user_id": "3eda55bf-d9cc-4cc8-a7bd-f74953fbb4dd"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jesus Gardener Daniel Perry",
            "has_profile_photo": false,
            "user_id": "3f8002af-5b70-400d-a75b-48f3df9b8e00"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Art Marble & Tile Rutillo Hernandez Arleen Lively",
            "has_profile_photo": false,
            "user_id": "3f907f92-39a6-4483-9fbd-cc0281056283"
        },
        {
            "email": "rainammolla@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Raina Molla",
            "has_profile_photo": false,
            "user_id": "3fcf105e-2a05-4d54-9497-3c474a8982d0"
        },
        {
            "email": "wallstreetermv@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mike Victor",
            "has_profile_photo": false,
            "user_id": "4008ea03-ae30-4f24-9ced-030230d8a22c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "GUADALUPE IBARRA KELLEY SCUTELNICU",
            "has_profile_photo": false,
            "user_id": "4036a9ab-06e9-4ca9-8f61-b1ecdf971867"
        },
        {
            "email": "steve@advoque.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Steve Hermosillo",
            "has_profile_photo": false,
            "user_id": "40788575-4e0b-4cb3-bf54-a4a0ed0ad03f"
        },
        {
            "email": "gawonnshinn@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jordan Shin",
            "has_profile_photo": false,
            "user_id": "40fdefa9-acad-41af-957e-282db8eb3908"
        },
        {
            "email": "morganperez@aol.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Morgan Perez",
            "has_profile_photo": false,
            "user_id": "410afe42-1769-4aec-84f9-05865b957566"
        },
        {
            "email": "ddm8000@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Diana DiNucci-Maher",
            "has_profile_photo": false,
            "user_id": "414b6f77-b3ad-4848-a13c-75c51f419aad"
        },
        {
            "email": "skhanijow13@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sonia Jackson",
            "has_profile_photo": false,
            "user_id": "416de308-f3d5-47a1-81ff-f6eb818ebcea"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Lauri Wrona",
            "has_profile_photo": false,
            "user_id": "41db39ad-3598-4dfb-87b6-079f4ecc62c5"
        },
        {
            "email": "fdinucci.fix@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Farrah DiNucci-Maher",
            "has_profile_photo": false,
            "user_id": "41fd89c7-2b4e-4dc5-a0b1-f9780c91234b"
        },
        {
            "email": "anton33@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "22 Crystal Ridge Drive",
            "has_profile_photo": false,
            "user_id": "430d6119-86a1-4092-b3ad-10a24d514dc9"
        },
        {
            "email": "devin.minkoff@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Devin Minkoff",
            "has_profile_photo": false,
            "user_id": "443909df-d7ce-4bf4-90a4-6151ce21f918"
        },
        {
            "email": "vlostetter@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Vincent Lostetter",
            "has_profile_photo": false,
            "user_id": "446d6614-2474-48b2-8ad9-c7c24ef518b5"
        },
        {
            "email": "rc@listerconstruction.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ron Lister",
            "has_profile_photo": false,
            "user_id": "447c7d28-9fbf-404c-8092-28951e293241"
        },
        {
            "email": "garcia89@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Alex & Jaqueline Garcia",
            "has_profile_photo": false,
            "user_id": "44bab09e-8fa9-4161-892c-d6b2ce3a9fbf"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "cleaning lady Lugo Fernando",
            "has_profile_photo": false,
            "user_id": "45630651-8189-40ea-9ecb-48e6b4a08e90"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cabinet install Crese Aldaba Arleen Lively",
            "has_profile_photo": false,
            "user_id": "4591cb35-f247-40bc-8698-0685a291c67e"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gardener Ben Errez",
            "has_profile_photo": false,
            "user_id": "466dfdaf-fa75-430c-a4d9-d64fc86e134e"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock Heavens",
            "has_profile_photo": false,
            "user_id": "4694eb01-4a92-4192-898d-c61999adf7b1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Wissam Elfarra",
            "has_profile_photo": false,
            "user_id": "46b2d6a2-a60f-445b-a63b-516eff5ae23f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kayla Calkins",
            "has_profile_photo": false,
            "user_id": "46d14bfe-29df-4bc5-9ebd-fbf7fe3c7ddb"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Carmen Anderson",
            "has_profile_photo": false,
            "user_id": "4768e544-0b06-4933-bf40-c27b2d1db528"
        },
        {
            "email": "kfurgie@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Katie DeMaria",
            "has_profile_photo": false,
            "user_id": "48e429ce-6401-4b3a-8603-f88b17f41ef6"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "United Parcel Services",
            "has_profile_photo": false,
            "user_id": "4950297c-7ab0-463e-9b84-5fe33a91d84c"
        },
        {
            "email": "kvcarranza@gscconcrete.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Vanessa Carranza",
            "has_profile_photo": false,
            "user_id": "498363ad-bca1-4675-9d45-7dc3df7e9863"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gardener Morgan Perez",
            "has_profile_photo": false,
            "user_id": "4a056cc6-1054-4f75-9f17-37eb48b4fe66"
        },
        {
            "email": "forrest@fdrconstruction.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Forrest Reardon",
            "has_profile_photo": false,
            "user_id": "4a46804d-d194-48bc-b97e-720e2a131114"
        },
        {
            "email": "katyzhi@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Yuan Yuan Zhi",
            "has_profile_photo": false,
            "user_id": "4a53038f-ba6a-4950-8734-56d98ac56539"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Estela Dysterheft Allegra Martins",
            "has_profile_photo": false,
            "user_id": "4a5e6d26-2182-4ffc-bce0-7ee2ae6caf0a"
        },
        {
            "email": "juli-accounting@sabresciences.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "27 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "4afbc282-c8b3-4e3f-a9ab-1bb07d78ead8"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cindy Payne",
            "has_profile_photo": false,
            "user_id": "4b409de5-9d47-4338-b062-5682a4055059"
        },
        {
            "email": "rosy0612_1990@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rosalinda Baza Madrigal Byung Kang",
            "has_profile_photo": false,
            "user_id": "4b411c60-4ae8-451e-a35b-627cdabc78bb"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Paula Concannon",
            "has_profile_photo": false,
            "user_id": "4ba950dc-3f5e-4258-be48-0d58e867dff2"
        },
        {
            "email": "louise_rollins@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Louise Rollins",
            "has_profile_photo": false,
            "user_id": "4bcba956-fc25-437e-bda1-ce5c6e84b5dd"
        },
        {
            "email": "robcofsd@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Robert Concannon",
            "has_profile_photo": false,
            "user_id": "4bfaec1d-e8ef-4ee4-a586-8aba2f640789"
        },
        {
            "email": "djokodal@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ryan Sun",
            "has_profile_photo": false,
            "user_id": "4c878e4c-02de-4f74-a81c-7fc8c1e8c419"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Griselda Gaytan Jennie Concannon",
            "has_profile_photo": false,
            "user_id": "4d30d04f-37dd-459d-b447-a6f9befaf1ca"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sami Faqih",
            "has_profile_photo": false,
            "user_id": "4e201f90-9075-4bbc-9062-74b559986e34"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Carrol Montemuro",
            "has_profile_photo": false,
            "user_id": "4e21e352-6c4a-47b5-8fef-409c749c4fc5"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock Heavens",
            "has_profile_photo": false,
            "user_id": "4e501f90-d173-4192-a696-536b762a56d0"
        },
        {
            "email": "joe@gscconcrete.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Joe Davitt",
            "has_profile_photo": false,
            "user_id": "4ed05129-7f56-428e-bf18-ea597361c3e4"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Son-in-law Honz",
            "has_profile_photo": false,
            "user_id": "4ed62816-69a5-4575-ba8c-412e13ea0180"
        },
        {
            "email": "srikovi@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Srinivasa Kovi",
            "has_profile_photo": false,
            "user_id": "4ef7ec9f-4b3c-4d7e-8ce7-106371655eef"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Adrian Zarty Arleen Lively",
            "has_profile_photo": false,
            "user_id": "4fcb71ff-2272-40cf-876a-a545c7a60c34"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Premteerth Sawh",
            "has_profile_photo": false,
            "user_id": "4ff818ca-7d91-4fb5-9250-ae6e3804a841"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Farrah Cristini",
            "has_profile_photo": false,
            "user_id": "5046a45b-8729-461b-8308-faa9dfe26302"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Eddie Gomez Home Front Ent Arleen Lively",
            "has_profile_photo": false,
            "user_id": "504aaf16-1e4b-4a95-92f2-980c53b1905b"
        },
        {
            "email": "ginarae11@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gina Goodwin",
            "has_profile_photo": false,
            "user_id": "505476e3-4679-4567-b16a-0378d2309b64"
        },
        {
            "email": "yidnek74@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Yidnek Meferia",
            "has_profile_photo": false,
            "user_id": "5077e544-69f3-4853-be22-d3aa0d12950d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Brook Daniel",
            "has_profile_photo": false,
            "user_id": "52445207-0021-4bd6-b603-7bf3f3d86f82"
        },
        {
            "email": "ty@corsecurity.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "COR Security (Backup)",
            "has_profile_photo": false,
            "user_id": "52b0f406-263b-4739-b9bc-70af9fd888fa"
        },
        {
            "email": "1rickmills@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rick Mills",
            "has_profile_photo": false,
            "user_id": "52ebfee4-18e4-490d-be79-55e5aed25b94"
        },
        {
            "email": "maggiegraves1995@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Maggie Graves",
            "has_profile_photo": false,
            "user_id": "53a43708-e07a-4640-97fb-a1d2473d11f8"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock Heavens",
            "has_profile_photo": false,
            "user_id": "53a4ae7a-25c0-4cb5-ab6d-d50888670ce1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mary Kate Lowe",
            "has_profile_photo": false,
            "user_id": "53d98d13-2c80-41e5-91e6-4c390f6cc828"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Keycard used by Ben Errez",
            "has_profile_photo": false,
            "user_id": "53e96370-0a18-4898-ab89-f7a3d39c57c1"
        },
        {
            "email": "millikenlauren@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Lauren Hagglund",
            "has_profile_photo": false,
            "user_id": "54ee8679-d596-459a-9781-dee1ff61294d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gerald (Jerry) Granger",
            "has_profile_photo": false,
            "user_id": "569c435d-354f-40ea-a801-7104e8fd9c09"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Tiffany Newberry",
            "has_profile_photo": false,
            "user_id": "576af5f0-1697-4771-b4d7-47c75ecdd810"
        },
        {
            "email": "jeffrey@360rez.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jeff O'Neil Robin Hudson Torme",
            "has_profile_photo": false,
            "user_id": "57e16bec-b325-4376-85a2-d135085ff49a"
        },
        {
            "email": "zdan15@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Zack Daniel",
            "has_profile_photo": false,
            "user_id": "583d1367-f372-4e22-a9d4-017781f567a8"
        },
        {
            "email": "tzarza@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Timothy Zarza",
            "has_profile_photo": false,
            "user_id": "583f3c20-e0c8-4eaa-b90d-ca973d8f0bfb"
        },
        {
            "email": "ryderzpaxton@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ryder Paxton",
            "has_profile_photo": false,
            "user_id": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Eric Richey pool Rosa Zonzales",
            "has_profile_photo": false,
            "user_id": "596c0e19-3349-4056-8a67-5794d1241de3"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Orkin Pest Fernando Lugo",
            "has_profile_photo": false,
            "user_id": "5980ec3c-bc18-47ba-aa39-ceb43076b8c3"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock Heavens",
            "has_profile_photo": false,
            "user_id": "59a03038-f6c7-4d21-8149-db6755b7e046"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Art's Marble Gustavo Garcia Arleen Lively",
            "has_profile_photo": false,
            "user_id": "59b3086b-7593-42a2-b846-aaeda464ed6d"
        },
        {
            "email": "sk.arsenault@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "29528 Welk Highland Drive",
            "has_profile_photo": false,
            "user_id": "5a9774ec-1da2-4b5f-810b-8b651fa0bd05"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sheriff San Diego County",
            "has_profile_photo": false,
            "user_id": "5c08b841-8fce-4217-b7b2-126fa91d1999"
        },
        {
            "email": "jnyablon@aol.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "29432 Welk Highland Drive",
            "has_profile_photo": false,
            "user_id": "5cace463-77c4-4c34-be78-2af9fdbdbf55"
        },
        {
            "email": "rhyanschmidt@outlook.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rhyan Siaweleski",
            "has_profile_photo": false,
            "user_id": "5cce7509-2a02-40a4-a4c8-fdc48745674d"
        },
        {
            "email": "curtis.gwa@att.net",
            "employee_id": "",
            "external_id": "",
            "full_name": "Curtis Lively",
            "has_profile_photo": false,
            "user_id": "5da556cd-78dc-46e2-b54b-929eae815868"
        },
        {
            "email": "thirdthorn@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Todd Wells",
            "has_profile_photo": false,
            "user_id": "5e03be51-9877-4586-a7b6-b54c35c4feb8"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Romero Painting Jesus Lastre Arleen Lively",
            "has_profile_photo": false,
            "user_id": "5e1b9811-5071-4514-a32f-b14b621c9e3d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock no activity Heavens",
            "has_profile_photo": false,
            "user_id": "5e6e4da3-bc60-4ff3-8aff-a2d72d42d7df"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pun Thompson",
            "has_profile_photo": false,
            "user_id": "5e80bf27-a4d5-40e4-acf8-da6cbccef3cb"
        },
        {
            "email": "cedarrockadvtures@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock no activity Heavens",
            "has_profile_photo": false,
            "user_id": "5eee076d-1dcf-46d7-afc2-dca617a7409e"
        },
        {
            "email": "gabriellegialet@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Big Parties",
            "has_profile_photo": false,
            "user_id": "5f89d5fb-9ace-456a-ae55-f23d7176267b"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Maria Ramirez Daniel Perry",
            "has_profile_photo": false,
            "user_id": "5fa7fa88-e7e6-4e24-93b3-a15e5a3edebf"
        },
        {
            "email": "camelias.spaces@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Aida Garcia Stu Oster",
            "has_profile_photo": false,
            "user_id": "6000bd19-3855-44f8-b2bf-008fa888d18a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pam Owen",
            "has_profile_photo": false,
            "user_id": "60e50f5a-3370-4e75-b72b-a3eff75b8776"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Patricia Rodriguez",
            "has_profile_photo": false,
            "user_id": "6108de5d-36fb-4de2-80dd-aea878338b04"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "cleaning lady Firat Ozkan",
            "has_profile_photo": false,
            "user_id": "613c5c53-3c3f-4034-9054-e4d096ca39fe"
        },
        {
            "email": "mateoanand@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mateo Anand",
            "has_profile_photo": false,
            "user_id": "617fd012-5369-4b04-8a7a-7fa2c16556ff"
        },
        {
            "email": "logancscully@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Logan Scully",
            "has_profile_photo": false,
            "user_id": "6251a0a3-257c-459d-9948-15f6aceed68f"
        },
        {
            "email": "spfurgie@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Scott Furgerson",
            "has_profile_photo": false,
            "user_id": "6346bcc7-7cdc-40ae-8ecc-7281d403402a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Quincy Thompson",
            "has_profile_photo": false,
            "user_id": "638b59a2-889e-41f3-a6f2-9610e2f90419"
        },
        {
            "email": "photosteves@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Stephen Sunseri",
            "has_profile_photo": false,
            "user_id": "64c0ef5b-3e80-4d71-b200-5eb206c87659"
        },
        {
            "email": "karla_fern@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Karla Hernandaz",
            "has_profile_photo": false,
            "user_id": "64ef6a59-bbc5-48fb-8e1a-ded9760b0537"
        },
        {
            "email": "jessicacerikson@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jessica Ericson",
            "has_profile_photo": false,
            "user_id": "6567033a-b29d-454a-8f30-6e217d2ba271"
        },
        {
            "email": "tahirymadina@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Madina Tahiry",
            "has_profile_photo": false,
            "user_id": "65de5d03-a05b-41a8-802d-a8813f110625"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Patrict Restrooms Nacho Cewantes Arleen Lively",
            "has_profile_photo": false,
            "user_id": "65e08f20-aabe-4aa3-83e3-5282f1812650"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cleaning lady Natasha Bailey Sawh",
            "has_profile_photo": false,
            "user_id": "66656b70-948b-4140-b863-87e692220f49"
        },
        {
            "email": "chrisagpestcontrol@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Chris Ag Pest Control",
            "has_profile_photo": false,
            "user_id": "66671d7d-3e75-4547-a8de-28b8236b8c5d"
        },
        {
            "email": "izzyhermosillo999@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Izzy Hermosillo",
            "has_profile_photo": false,
            "user_id": "66d560ac-7866-4f07-a68f-b80bea9c7a47"
        },
        {
            "email": "steveconcannon62@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Steve Concannon",
            "has_profile_photo": false,
            "user_id": "66da2ca5-8e70-46f9-b9d2-03828414d8e0"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Nohealani Martins",
            "has_profile_photo": false,
            "user_id": "66e61df9-0869-4034-861b-18a91f1e827a"
        },
        {
            "email": "duiphil@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Phil Colonnelli",
            "has_profile_photo": false,
            "user_id": "66f35808-8fbb-4c46-9966-a8f94912e1b4"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "HomeFront Ent Mario Hefer Arleen Lively",
            "has_profile_photo": false,
            "user_id": "672dcc5b-f44d-46de-bc62-c7040e45dda8"
        },
        {
            "email": "bigmacmartin32@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Martin Wronski",
            "has_profile_photo": false,
            "user_id": "67cc415d-9d0b-4ae5-bb7c-303ec4724d13"
        },
        {
            "email": "rimrockaccess@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Carrie Hartwick",
            "has_profile_photo": false,
            "user_id": "68358276-bc7f-420b-b8eb-d63177a97b11"
        },
        {
            "email": "sleepdoc2@me.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rick Engel",
            "has_profile_photo": false,
            "user_id": "6a674d9f-be89-49bb-9616-e01aecec60e9"
        },
        {
            "email": "kkorinek@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kimberly Korinek",
            "has_profile_photo": false,
            "user_id": "6a9ec4d7-f578-487c-b0b9-e7f392034663"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Federal Express",
            "has_profile_photo": false,
            "user_id": "6aa7e1d8-049f-4792-921a-147498dd3620"
        },
        {
            "email": "jccastellanos59.jc@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jose Cruz Stu Oster",
            "has_profile_photo": false,
            "user_id": "6ab7e09c-5c78-483d-8778-fd7e9ed15ec9"
        },
        {
            "email": "kyryx69@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Richard Mallo",
            "has_profile_photo": false,
            "user_id": "6acdde8a-a6fd-403f-99fd-2402dab5bd98"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Fedrico Mondragon Landscape Martin Wronski",
            "has_profile_photo": false,
            "user_id": "6b0081d3-b5e1-4cac-a815-0b53c4de569c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Joy Maze",
            "has_profile_photo": false,
            "user_id": "6b8768c2-87dc-492c-a9a8-82b6ab34aee1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Alan Saywer",
            "has_profile_photo": false,
            "user_id": "6c302ea8-72d4-4917-83d5-9520c99f09ff"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Yurayh Velazquez",
            "has_profile_photo": false,
            "user_id": "6c67a6f9-de5b-4f68-ba2f-076c2957b1b4"
        },
        {
            "email": "Gene@gscconcrete.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gene Carranza",
            "has_profile_photo": false,
            "user_id": "6d5d477c-745b-4f4a-a393-403e7225ce6c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rosa Beltran",
            "has_profile_photo": false,
            "user_id": "6ebb35ba-b2b1-4480-b594-3a28df7b97ef"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "contractor Tony Hughes Martin Wronski",
            "has_profile_photo": false,
            "user_id": "6f4dde9c-e453-4445-a3c1-b94b30d57978"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock no activity Heavens",
            "has_profile_photo": false,
            "user_id": "7001ce7a-b24c-42c3-8962-dde42efc9ad8"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Tiffany Nelson",
            "has_profile_photo": false,
            "user_id": "7072db01-6b4a-4eca-a8d6-e27626bbdd7d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jennie Concannon",
            "has_profile_photo": false,
            "user_id": "7075a5d2-8ceb-4056-950d-ca175a07804b"
        },
        {
            "email": "sewiquilt@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Linda Fornaca",
            "has_profile_photo": false,
            "user_id": "70c37aa7-01f5-42c2-b951-3b80845181f4"
        },
        {
            "email": "bkaep2@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Brittany Palmer",
            "has_profile_photo": false,
            "user_id": "70edc7ba-9fef-4c04-afb6-f3219e19ebcd"
        },
        {
            "email": "sobh2455@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jay Sobh",
            "has_profile_photo": false,
            "user_id": "7151ee03-3241-4ddc-ab09-3bc48d570bfc"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Romero Paint Able Compo Arleen Lively",
            "has_profile_photo": false,
            "user_id": "71656457-e7b8-4708-9ad8-060fc40e08b3"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Augustine Martinez Arleen Lively",
            "has_profile_photo": false,
            "user_id": "717cd345-80e0-4e37-a7a3-f7ddc75552d9"
        },
        {
            "email": "linaamolla@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Lina Molla",
            "has_profile_photo": false,
            "user_id": "72132ea0-fa61-445c-ad55-6f208ff95b2e"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "IT Richardo Buhain Arleen Lively",
            "has_profile_photo": false,
            "user_id": "724d367b-6eac-4078-919f-29aa062f7a13"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kristen Korinek",
            "has_profile_photo": false,
            "user_id": "725d043e-e035-4d87-bc16-3fda95a0d6ae"
        },
        {
            "email": "jill.prantera@heraeus.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jill Prantera",
            "has_profile_photo": false,
            "user_id": "728e6af4-bd0f-4f1d-b373-daf4d51c0ee2"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ashok Khanijow",
            "has_profile_photo": false,
            "user_id": "73161f28-943d-42c2-ae8e-08c1528e9c3c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Martiniz Landscape James Shin",
            "has_profile_photo": false,
            "user_id": "7338c261-a33a-4ce0-a074-4b767c67f0b9"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Maria Rodriguez",
            "has_profile_photo": false,
            "user_id": "737186eb-f10a-4c3b-8922-991bb82cd4ee"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "great White Pool Ellen Molla",
            "has_profile_photo": false,
            "user_id": "73c2269f-7540-467b-afa1-1c8135756e78"
        },
        {
            "email": "jimmy92026@outlook.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jim Urbina",
            "has_profile_photo": false,
            "user_id": "74cd95d3-dced-41ec-83ff-81660ce3c8bb"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "master shower pan Emilo Arleen Lively",
            "has_profile_photo": false,
            "user_id": "74ed8924-896d-46bf-aad0-bf0546ff67dd"
        },
        {
            "email": "Octavian@arcstonebuilders.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "OCTAVIAN SCUTELNICU",
            "has_profile_photo": false,
            "user_id": "74f77331-8186-4c89-80aa-80e46b4150b6"
        },
        {
            "email": "david@diversifiedhospitality.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "David Garcia",
            "has_profile_photo": false,
            "user_id": "7552299f-38e4-4e8c-92b4-be84b93ba2f7"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "sherri Mellor",
            "has_profile_photo": false,
            "user_id": "7557657f-124a-4657-9eee-eca2b83821dc"
        },
        {
            "email": "Hanaymolla@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Hana Molla",
            "has_profile_photo": false,
            "user_id": "759057f4-ca3f-4670-b019-18ee8e19ffe2"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "GL Pools Siaweleski",
            "has_profile_photo": false,
            "user_id": "75cd59cf-9b25-4ea5-8a3d-ed8b9f66435a"
        },
        {
            "email": "David.Fimon@fire.ca.gov",
            "employee_id": "",
            "external_id": "",
            "full_name": "Deer Spring Fire Truck",
            "has_profile_photo": false,
            "user_id": "771e583b-7199-4449-8e20-9dd977fd5f4c"
        },
        {
            "email": "clarencejd6@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Clarence DeLeon",
            "has_profile_photo": false,
            "user_id": "773c447a-3eb2-43c0-914e-7e1f2a83126d"
        },
        {
            "email": "robcarpenter4@cox.net",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rob Carpenter",
            "has_profile_photo": false,
            "user_id": "77b2f875-8f11-4081-b1f3-5f32be20b1a6"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Dwayne Allen Plumbing Arleen Lively",
            "has_profile_photo": false,
            "user_id": "77cad767-37b0-4389-9af1-0a370b6f8c98"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Forrest #2 Reardon",
            "has_profile_photo": false,
            "user_id": "78dd7916-56b9-4494-a2c7-55c67359fbc0"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cleaning lady Hal Bassett",
            "has_profile_photo": false,
            "user_id": "78e13f7d-f43e-4d26-ad4c-cad8f7e70c93"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sean Aqua Oasis Gregson",
            "has_profile_photo": false,
            "user_id": "78ed1bf2-01fb-4c20-953c-50b52d73183a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Fallbrook Propane",
            "has_profile_photo": false,
            "user_id": "798cac72-9088-4c94-8393-0b065e4cdf76"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ana Lilia Kathleen Delmastro",
            "has_profile_photo": false,
            "user_id": "7a7eeacd-2103-41f8-81aa-b66547405f0f"
        },
        {
            "email": "chris.minkoff@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Chris Minkoff",
            "has_profile_photo": false,
            "user_id": "7abb65cc-0d27-4cb0-a57d-f0e719c69274"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Anastasia Housekeeping Furgerson",
            "has_profile_photo": false,
            "user_id": "7b85a61a-bd1c-417e-8df4-e2436f760645"
        },
        {
            "email": "huaijunhuaixiang@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Patrick Sun",
            "has_profile_photo": false,
            "user_id": "7c019096-3da3-411a-b2b1-1d8aabe8ea11"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Grandson Honz",
            "has_profile_photo": false,
            "user_id": "7ca74a0c-a240-4678-a70f-2c4d2cde53eb"
        },
        {
            "email": "support+corsecurity+1732058573@verkada.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Verkada Support",
            "has_profile_photo": false,
            "user_id": "7d0d5402-e8b4-4245-aa2c-12d9ceaf74ed"
        },
        {
            "email": "sammybug73@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sam Bergstrom Samarvedey",
            "has_profile_photo": false,
            "user_id": "7deb8bb3-3b73-4731-abf9-9245878e0507"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Francisco Lopez Loma Alta Landscape Marsha Michael",
            "has_profile_photo": false,
            "user_id": "7e25c91c-1948-41e8-b311-4acf2761bbf2"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Landscaper John DelMastro",
            "has_profile_photo": false,
            "user_id": "7e4ed36a-7a6d-4d4b-97c2-a6fbe7872ea3"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Carlos Gardener Karla Hernandaz",
            "has_profile_photo": false,
            "user_id": "7e8becaa-f06c-47b9-b4f1-b3848ab40d1e"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "CertaPro Dan Carrie Hartwick",
            "has_profile_photo": false,
            "user_id": "7ef607ff-c3f5-4216-9a39-8f53f4d52776"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Juan Rocha Kent Schafer",
            "has_profile_photo": false,
            "user_id": "7f406cce-8d55-458f-a6ad-317c68b04796"
        },
        {
            "email": "pgregson@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Penny Gregson",
            "has_profile_photo": false,
            "user_id": "7f65a4c2-f69a-4e99-8889-979491b8e062"
        },
        {
            "email": "maingatelisa@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Lisa Maingate",
            "has_profile_photo": false,
            "user_id": "7f6ed324-b298-46b4-b459-fb848fa3c96f"
        },
        {
            "email": "model1968@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Noveline Mallo",
            "has_profile_photo": false,
            "user_id": "7f8fbb76-5fe1-4a3d-b8f6-e24e48d0ae1f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Tino Diego Gardener Peter Kim",
            "has_profile_photo": false,
            "user_id": "8008acc4-655f-452c-8541-9b746542ddf3"
        },
        {
            "email": "jeokiki@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sera Rhee",
            "has_profile_photo": false,
            "user_id": "8030f609-b19a-4920-9ff9-9587eb53c140"
        },
        {
            "email": "2isaiah.ramos4@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Isaiah Ramos",
            "has_profile_photo": false,
            "user_id": "80b485fc-3aab-4b62-ab34-8dcdbc003ee4"
        },
        {
            "email": "resobrian@cox.net",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rita O'Brien",
            "has_profile_photo": false,
            "user_id": "81360824-b40f-4b18-b62f-ae935596364f"
        },
        {
            "email": "richardsonwh@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Walter Richardson",
            "has_profile_photo": false,
            "user_id": "819d88ab-54f2-4da0-8e07-a0ed1eecfac6"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock no activity Heavens",
            "has_profile_photo": false,
            "user_id": "8271bfea-b7d3-428d-b466-c729ca13ff7c"
        },
        {
            "email": "ramonocampo75@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ramon Ocampo",
            "has_profile_photo": false,
            "user_id": "82d24312-09a3-441f-9d08-cc46228845ed"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Power Pet Adam Levy",
            "has_profile_photo": false,
            "user_id": "839e0ecf-765a-45a9-b095-9c3d005a467c"
        },
        {
            "email": "rimrockguards@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rimrock guard",
            "has_profile_photo": false,
            "user_id": "847d5d0a-b5b2-4f82-b8b9-1e24d2a3f93d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mike Concannon",
            "has_profile_photo": false,
            "user_id": "858cc14f-12ec-4b86-8190-36dadd792d7b"
        },
        {
            "email": "aishakakar@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Aisha Kakar",
            "has_profile_photo": false,
            "user_id": "86380e0c-909c-4350-b193-6a2ffb1fb094"
        },
        {
            "email": "anshengwang08@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "AnSheng Wang",
            "has_profile_photo": false,
            "user_id": "86b6d056-7c78-47fa-b423-9cc14e2c9b4a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jorge Flores CRC Engineering",
            "has_profile_photo": false,
            "user_id": "86dafc0d-516e-440e-8ecf-0fe5e7a9121e"
        },
        {
            "email": "robert.tahiry@brightstarcare.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Robert Tahiry",
            "has_profile_photo": false,
            "user_id": "86e1d26e-73bb-44e6-86c3-8193afa9e2ba"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "S&A Pool Andy Adam Levy",
            "has_profile_photo": false,
            "user_id": "870cbe00-ff49-4100-a63f-bbea8cdbba7a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Art Marble & Tile San Gonzales Arleen Lively",
            "has_profile_photo": false,
            "user_id": "87adf3f9-e210-424e-8ab9-c59d455a322f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Andres Reyes Landscape Mary Kate Lowe",
            "has_profile_photo": false,
            "user_id": "88077156-b233-45bf-8fee-228c2fa3dacc"
        },
        {
            "email": "rmschafer.srdailey@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rose Schafer",
            "has_profile_photo": false,
            "user_id": "8851adfa-3a22-4447-94fd-745e5e42cd57"
        },
        {
            "email": "helena.kim374@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Helena Kim",
            "has_profile_photo": false,
            "user_id": "88f033d9-7342-4cc4-a2e9-7e341ad1c6cf"
        },
        {
            "email": "mcouper99@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Marc Wrona",
            "has_profile_photo": false,
            "user_id": "890f1296-6069-45d4-a46b-2fda55ec53b8"
        },
        {
            "email": "brendadupa2004@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Brendaly Ring",
            "has_profile_photo": false,
            "user_id": "89503d3f-7715-41fe-a095-a2383ed1e1b0"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sergio Garcia Gardener Richardson",
            "has_profile_photo": false,
            "user_id": "89802508-b38a-4c74-aa15-5c78efaaf6db"
        },
        {
            "email": "ddrinan@philometron.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Darrel Drinan",
            "has_profile_photo": false,
            "user_id": "89acf4c7-7e7e-4d7f-88a6-5971fd7184ea"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pia Courser",
            "has_profile_photo": false,
            "user_id": "89ae8f58-c0c9-456b-a931-4b7e45eb140d"
        },
        {
            "email": "bob.marrero.jr@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Bob Marrero",
            "has_profile_photo": false,
            "user_id": "8a0c152d-13c2-499e-aa4d-d087ce7812fb"
        },
        {
            "email": "leanne@auntiepasto.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Leanne Opaskar",
            "has_profile_photo": false,
            "user_id": "8a66b4f3-2d4e-4f06-8522-8947beddf2ba"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cleaning lady Sarah Graves",
            "has_profile_photo": false,
            "user_id": "8adca059-444b-4b25-ae8a-761d5af6d14b"
        },
        {
            "email": "mdureau@sbcglobal.net",
            "employee_id": "",
            "external_id": "",
            "full_name": "101 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "8ba28599-7965-46b2-bdfe-0651c80a2937"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Eric Anderson Engineering Arleen Lively",
            "has_profile_photo": false,
            "user_id": "8c111ca5-7aa1-453d-851b-b4a54fecedac"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mateo Landscape Hal Bassett",
            "has_profile_photo": false,
            "user_id": "8c5edae3-43fb-406f-adf7-9e558d285bed"
        },
        {
            "email": "magy.marrero.2@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Magy Marrero",
            "has_profile_photo": false,
            "user_id": "8d735295-8f5d-4a24-846a-d19d8c6e2ad0"
        },
        {
            "email": "sarahgraves59@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sarah Graves",
            "has_profile_photo": false,
            "user_id": "8db22411-d689-4847-8f39-8972e5522a9d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kathy Ochoa",
            "has_profile_photo": false,
            "user_id": "8dd1e877-d1a2-4e00-8825-bf1ceb1f7595"
        },
        {
            "email": "brent@shafranrealty.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Brent Hansen",
            "has_profile_photo": false,
            "user_id": "8e9606df-3c17-4d61-8f76-d3f330a66991"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock #1 Heavens",
            "has_profile_photo": false,
            "user_id": "8ec5056b-653a-49cf-9c63-24dc5370e590"
        },
        {
            "email": "dannielle.rimrock@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Dannielle Milliken",
            "has_profile_photo": false,
            "user_id": "8ec99223-25a3-4ecf-8b7c-52078294979f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Art's Marble Gonzales Arleen Lively",
            "has_profile_photo": false,
            "user_id": "8ede26bf-8db7-4823-af10-9127e4dc2efd"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ranin Alnajjar",
            "has_profile_photo": false,
            "user_id": "8f27fb15-fc43-4ef6-9fc4-e1e1cfd17046"
        },
        {
            "email": "lsandie@scmsonline.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Silverado Management",
            "has_profile_photo": false,
            "user_id": "900f26bd-8216-44d9-8084-897a7a86c8e5"
        },
        {
            "email": "info@corsecurity.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "COR Security",
            "has_profile_photo": false,
            "user_id": "90594583-b92c-48ea-9186-fa4b2d7e06ef"
        },
        {
            "email": "vis@sabresciences.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Michael (Micky) ??? Montemuro???",
            "has_profile_photo": false,
            "user_id": "909a5a3f-af95-4fbb-9e7a-47041b62f742"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Katherine Fernandez",
            "has_profile_photo": false,
            "user_id": "90bb36ec-8518-4d25-a1e1-e1f74f153be2"
        },
        {
            "email": "adachi25@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Youngjoo Shin",
            "has_profile_photo": false,
            "user_id": "90f56854-db4d-43b4-b4c3-57f5f4ffc87c"
        },
        {
            "email": "kaxonknievel@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jaxon Knievel tenant Mary Kate Lowe",
            "has_profile_photo": false,
            "user_id": "90f75ebe-a2b1-45c8-9b3d-97d51677e53c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Christopher Siaweleski",
            "has_profile_photo": false,
            "user_id": "91b934cc-2e77-4d3f-be44-cee20486e0e8"
        },
        {
            "email": "landscapingpacheco02@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pacheco Landscaping (Noveline Mallo)",
            "has_profile_photo": false,
            "user_id": "9222227c-efa2-43ec-83a3-2fdb3e9b5cc3"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Leann Baker cleaning lady Izzy Hermosillo",
            "has_profile_photo": false,
            "user_id": "92727d20-03a0-4b35-ba4b-525beacdd87f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Timmy Milliken",
            "has_profile_photo": false,
            "user_id": "927860bb-b1bb-45c3-9e73-0aaa3a9b505e"
        },
        {
            "email": "svillariasa@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Steve Villariasa",
            "has_profile_photo": false,
            "user_id": "9288df25-ff11-4f3b-8a2e-1e0452ac4922"
        },
        {
            "email": "olivesikem@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "48 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "92a417b8-bc7c-4eb3-8d2b-147e353b1232"
        },
        {
            "email": "jdelmast69@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "John Delmastro",
            "has_profile_photo": false,
            "user_id": "92dac28b-916b-4215-a483-87feae7d2711"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ashytn Roney CRC Engineering",
            "has_profile_photo": false,
            "user_id": "93c20572-2405-47d4-9998-fde58136d55a"
        },
        {
            "email": "runitbydena@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Dena Williams",
            "has_profile_photo": false,
            "user_id": "93f602b3-b282-449b-a01d-0f069b42c8d4"
        },
        {
            "email": "peiran.lu7@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Peiran Lu",
            "has_profile_photo": false,
            "user_id": "950cc97d-8979-405f-9dd0-06a762005a60"
        },
        {
            "email": "danielperry1956@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Daniel Perry",
            "has_profile_photo": false,
            "user_id": "953c179b-45f4-42bf-82a1-77b0739b4472"
        },
        {
            "email": "rimrockheavens@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sri + another app user Heavens",
            "has_profile_photo": false,
            "user_id": "96429c52-4659-4506-8924-070d78a29ae1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cely Ramirez Noveline Mallo",
            "has_profile_photo": false,
            "user_id": "96bf9c9e-c247-404b-bcc9-f08b9494b120"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Romero Painting Alonso Resencliz Arleen Lively",
            "has_profile_photo": false,
            "user_id": "9726b439-cfb6-4e22-aa89-de4585b8a7bd"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "All Pest Pros Dawn Korinek",
            "has_profile_photo": false,
            "user_id": "9802fc96-b84a-46c3-8f5e-9702f645f3ca"
        },
        {
            "email": "vince@supercoolcreative.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Vincent Murdico",
            "has_profile_photo": false,
            "user_id": "98354ff0-fbe2-4f26-ae5e-5cf1b5e95568"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Marlucio Goncalves Da Silveira^",
            "has_profile_photo": false,
            "user_id": "9865d7b9-3f37-4b68-b235-682de54ed956"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Refreshing Pool & Spa Hal Bassett",
            "has_profile_photo": false,
            "user_id": "98933a27-b130-4c75-bbf4-02e13603fc80"
        },
        {
            "email": "gordonschafer@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gordon Schafer",
            "has_profile_photo": false,
            "user_id": "98f17656-7d30-490b-9b2c-2cdb276efb29"
        },
        {
            "email": "golfpeterkim@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Peter Kim",
            "has_profile_photo": false,
            "user_id": "99aa218c-393f-4ad5-bb9a-3a79ae311d12"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Demetrio Garcia Yoke Ho",
            "has_profile_photo": false,
            "user_id": "9a1397b4-5d56-44e9-8535-582738dbb50c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Alberto Pacheco Arnie Carter",
            "has_profile_photo": false,
            "user_id": "9a8f1058-e63f-4cc5-9ca3-7f2ffb36c8f8"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gustavo Escovedo gardener Juliet Navas",
            "has_profile_photo": false,
            "user_id": "9ac7237e-79fc-4c01-bf91-37a83e35fbc3"
        },
        {
            "email": "jaramirezinc@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Aurora Ramirez",
            "has_profile_photo": false,
            "user_id": "9afda9e2-8ea4-4899-979f-e1559b73e66a"
        },
        {
            "email": "palmer.linda@ymail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Linda Palmer",
            "has_profile_photo": false,
            "user_id": "9b06a458-523e-4e1f-8528-7223d5ad054a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Randall Ryden R&M Pool Fernando Lugo",
            "has_profile_photo": false,
            "user_id": "9b409389-afb1-4d11-a693-19d9fc6dcf33"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Antonio Silva Kang",
            "has_profile_photo": false,
            "user_id": "9b6a330e-c744-47bb-b76b-d705850b1d8f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sebastian Velasco Landscape Colleen Lister",
            "has_profile_photo": false,
            "user_id": "9bd142e9-f9aa-45dd-839d-ee10bdaeb1b1"
        },
        {
            "email": "joe.zlotnicki@3zconsulting.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Joe Zlotnicki",
            "has_profile_photo": false,
            "user_id": "9be65bc0-6a06-47e4-856e-6686a273be4c"
        },
        {
            "email": "gmabuzzy@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Buzz Oster",
            "has_profile_photo": false,
            "user_id": "9c0acf31-57d5-4258-a406-33ef36be6f17"
        },
        {
            "email": "Raquelitalugo@aol.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Raquelita Lugo",
            "has_profile_photo": false,
            "user_id": "9c17b638-4527-48e4-bcf0-57506a0adadd"
        },
        {
            "email": "mcouper99@golden-monkey.me",
            "employee_id": "",
            "external_id": "",
            "full_name": "Marc Wrona",
            "has_profile_photo": false,
            "user_id": "9c562d72-5ff1-4139-b09b-61e53031e24d"
        },
        {
            "email": "michaeleganskinner@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mike Skinner",
            "has_profile_photo": false,
            "user_id": "9c9720e6-17ad-47fd-9ce3-c9fdb329c3f0"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Freight Liner Arleen Lively",
            "has_profile_photo": false,
            "user_id": "9ca31c6a-8b8c-4f30-bba9-636fe1218781"
        },
        {
            "email": "kristiarnotti@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kristi Arnotti",
            "has_profile_photo": false,
            "user_id": "9d8eb244-2a09-4e96-97b5-92bbe8e6b82b"
        },
        {
            "email": "ryryx69@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Richard Mallo",
            "has_profile_photo": false,
            "user_id": "9dade04d-3f83-4f21-b44e-d10e56a3b336"
        },
        {
            "email": "darius.palmer1@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Darius Palmer",
            "has_profile_photo": false,
            "user_id": "9dd7d64e-8fad-4885-ab95-cc41551c7598"
        },
        {
            "email": "milliken1235@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Husband Milliken",
            "has_profile_photo": false,
            "user_id": "9e80788a-f798-4b1a-8254-cc91b4a9a546"
        },
        {
            "email": "akymproperties@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "AKYM Properties",
            "has_profile_photo": false,
            "user_id": "9ef5dda4-7822-4a57-a829-b70da9ef5fd5"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Andy #2 Etemadi",
            "has_profile_photo": false,
            "user_id": "9f31c3b5-aeab-47fd-b022-c01411dd6d66"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rosario Rocha Kent Schafer",
            "has_profile_photo": false,
            "user_id": "9f83ae4a-f7cc-43f0-8a7e-f07f314605cb"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Andres Reyes Landscape",
            "has_profile_photo": false,
            "user_id": "9fd7ad11-a6cd-45c3-9e38-a8892ac106b4"
        },
        {
            "email": "kyle@shafranrealty.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kyle Hansen",
            "has_profile_photo": false,
            "user_id": "a052357f-d987-4a3b-a816-13f0eb4bcaa7"
        },
        {
            "email": "rdinucci@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Richard Dementia Dinucci",
            "has_profile_photo": false,
            "user_id": "a15d1d78-84c3-40d8-81ee-723ffbbaaf78"
        },
        {
            "email": "pagek56@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kim Page",
            "has_profile_photo": false,
            "user_id": "a31a3330-cce2-45ff-8f5a-3d67d74a259a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "93 Welk Highland Drive",
            "has_profile_photo": false,
            "user_id": "a36f6a27-33e9-4fb6-98bb-eec9d7a964ad"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jamie Cristini",
            "has_profile_photo": false,
            "user_id": "a38639b0-d9bd-405c-b366-2d6bfd227af2"
        },
        {
            "email": "byungkang77@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Byung Kang",
            "has_profile_photo": false,
            "user_id": "a39d5527-6a80-4924-875f-6bdead8ad402"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mike Salm Arleen Lively",
            "has_profile_photo": false,
            "user_id": "a3a05f1a-0b8d-44ed-8d4e-2b9e2f84fe20"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Diane (sister) Lutz",
            "has_profile_photo": false,
            "user_id": "a3b2384a-d509-4e36-8c21-e24f8e8b8c09"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Marvin Ramirez",
            "has_profile_photo": false,
            "user_id": "a3eb3422-8028-4430-b046-3c7f3d718ac9"
        },
        {
            "email": "cnsinsurance@frontier.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cyril Honz",
            "has_profile_photo": false,
            "user_id": "a44308f5-b79c-4a2a-9dea-1b7a22863508"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Richard Mallo",
            "has_profile_photo": false,
            "user_id": "a4d0036e-fcf4-49d5-bfe7-84f25d9527de"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Larry CCC pool",
            "has_profile_photo": false,
            "user_id": "a6d1eaf3-47b0-4499-940b-3924d582b85c"
        },
        {
            "email": "mh6710868@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Miguel Hernandez",
            "has_profile_photo": false,
            "user_id": "a6daf024-1f0b-4517-af6e-a7e1ee2dfe5c"
        },
        {
            "email": "cfsnyderjr@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Charles Snyder",
            "has_profile_photo": false,
            "user_id": "a79f7a5f-0b18-4b23-be8e-3fc27686ddec"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "David Zipse Electrican Steve Hermosillo",
            "has_profile_photo": false,
            "user_id": "a814f0a5-7469-4070-8f6c-8d6fcf7bcafb"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gardener Natasha Bailey Sawh",
            "has_profile_photo": false,
            "user_id": "a8edc49c-60e2-422b-b4e2-285a3989f822"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kurt Mulhbach",
            "has_profile_photo": false,
            "user_id": "a98fe45c-1ef8-4553-8a89-75aedb08f42f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "visitor Anthony Gandolfo Izzy Hermosillo",
            "has_profile_photo": false,
            "user_id": "aad037f6-9a40-46cc-8e82-afe25a20643a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Madelyn Muhlbach",
            "has_profile_photo": false,
            "user_id": "abad0aef-4206-42fb-b7fb-d15b98dffed1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "BVI Solar Don Miller Arleen Lively",
            "has_profile_photo": false,
            "user_id": "ac4778d8-f648-4e24-b83e-5393591e85e8"
        },
        {
            "email": "lwrona@golden-monkey.me",
            "employee_id": "",
            "external_id": "",
            "full_name": "Laurie Wrona",
            "has_profile_photo": false,
            "user_id": "ac5f1c69-f593-4bd7-9a0e-b69ea5df8e8c"
        },
        {
            "email": "gary.bagheri@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gary Bagheri",
            "has_profile_photo": false,
            "user_id": "ad35e53d-feef-4864-ad20-78340104ce80"
        },
        {
            "email": "theandersens2015@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Shawn Anderson",
            "has_profile_photo": false,
            "user_id": "ad44d663-7ba8-4439-81c4-e7790c884a21"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Justin Calkins",
            "has_profile_photo": false,
            "user_id": "ad5e585d-165c-4d61-b0af-9f69ba35aece"
        },
        {
            "email": "annekangaroo@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Anne Kang",
            "has_profile_photo": false,
            "user_id": "ad7f95c8-2fa1-4b0c-950e-d73bce3e7684"
        },
        {
            "email": "katherinevillariasa@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Katherine Villariasa",
            "has_profile_photo": false,
            "user_id": "ae443d12-9380-49d7-8364-83ac18164678"
        },
        {
            "email": "mihyunshin1000@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mi Hyun Shin",
            "has_profile_photo": false,
            "user_id": "aef3f5c7-d5c2-43a8-b452-12b15ce080d6"
        },
        {
            "email": "sherigrant@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sheri Basinet",
            "has_profile_photo": false,
            "user_id": "aefbd6bb-9d24-4f30-a339-53c4d82ece2d"
        },
        {
            "email": "cedarrockventures@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Martin (1SKIDO) Wronski",
            "has_profile_photo": false,
            "user_id": "af2448bd-6e24-40f9-a4bd-09445614fe19"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pedro Alvaro Gregson gardener",
            "has_profile_photo": false,
            "user_id": "af39b8ba-008a-44e0-98cf-f4530c483121"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Manual Garcia Ramirez Latte Arleen Lively",
            "has_profile_photo": false,
            "user_id": "af6b7200-da9b-4790-aec2-dfe09b9d0476"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "48 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "afb3beda-310d-49b8-a732-5116fc618c83"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Diana designer Gregson",
            "has_profile_photo": false,
            "user_id": "afd07b41-22df-4bae-afb2-ae3e0b6a6e1a"
        },
        {
            "email": "sarafay1997@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sara Fayad",
            "has_profile_photo": false,
            "user_id": "b0082f4e-91bf-4a8d-be63-c2c07c2811eb"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mark Gregson Lot 66 #2",
            "has_profile_photo": false,
            "user_id": "b0153b0b-55ca-49f9-982e-f4d99ec0cee8"
        },
        {
            "email": "matthewanand@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Matthew Anand",
            "has_profile_photo": false,
            "user_id": "b02aab22-d059-4813-af21-0a3e718dba51"
        },
        {
            "email": "rangelrafael@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Angel Rangel",
            "has_profile_photo": false,
            "user_id": "b0ab6dd5-2d6b-45ef-95ec-2dd02638c370"
        },
        {
            "email": "jeffjohnsd@outlook.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jeff Johnston",
            "has_profile_photo": false,
            "user_id": "b1015b58-3ebc-442e-89a0-c250fb25b38e"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Terminix Colleen Lister",
            "has_profile_photo": false,
            "user_id": "b1686c82-1e97-4369-837d-fd461408a313"
        },
        {
            "email": "gm.arsenault@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "29528 Welk Highland Drive",
            "has_profile_photo": false,
            "user_id": "b1a150c6-a2fd-452a-a2e3-efbe711644fb"
        },
        {
            "email": "mercymarket@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mike Sobh",
            "has_profile_photo": false,
            "user_id": "b1e280ab-47b4-4f79-ab62-3168dea59300"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "VanBerg Construction Jim Fornaca",
            "has_profile_photo": false,
            "user_id": "b25caaea-4bec-4170-8f52-a894a794157c"
        },
        {
            "email": "erikaporter@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Erika Porter",
            "has_profile_photo": false,
            "user_id": "b276385a-c84f-4613-9e6c-b069cd6bd3bb"
        },
        {
            "email": "bkrissoff@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "William Krissoff",
            "has_profile_photo": false,
            "user_id": "b27ae11f-039b-46d0-a7f8-8ed35554f875"
        },
        {
            "email": "tduncan1960@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Tim Duncan Milliken",
            "has_profile_photo": false,
            "user_id": "b2c9542a-9082-4bd8-b7c7-bb726d92a6c9"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kelly Ramirez",
            "has_profile_photo": false,
            "user_id": "b2f56a7f-a47b-4889-9b8f-2d144bb735e4"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Fernando Bautista Handyman jaime Ramirez",
            "has_profile_photo": false,
            "user_id": "b2fb3fda-cfee-4895-90de-6c8b5878a10d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Patty Webster",
            "has_profile_photo": false,
            "user_id": "b31b6381-5abd-45bb-bc1f-3a0ec1e47ff5"
        },
        {
            "email": "trailside62@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Daniel Wanningen",
            "has_profile_photo": false,
            "user_id": "b33ed142-8333-4243-9cd6-4d7952ab6546"
        },
        {
            "email": "cdeco@me.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cynthia Engel",
            "has_profile_photo": false,
            "user_id": "b37d9ce9-6050-4871-ba0e-994d103ec263"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Elias Ortiz Gardener Jaime Ramirez",
            "has_profile_photo": false,
            "user_id": "b3d2915f-bb0b-4a15-b5db-231c2da05cff"
        },
        {
            "email": "kelley0503@msn.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kelley SCUTELNICU",
            "has_profile_photo": false,
            "user_id": "b42afbaa-aa91-425b-9ef7-5e17dbbc5bc0"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock no activity Heavens",
            "has_profile_photo": false,
            "user_id": "b453c494-008e-4db9-91db-e792387426c7"
        },
        {
            "email": "weijiachua@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Weijia Chua",
            "has_profile_photo": false,
            "user_id": "b48f2878-b232-4d3e-8125-71a160f7a075"
        },
        {
            "email": "choonchua@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Choon Chua",
            "has_profile_photo": false,
            "user_id": "b4a80a59-f4b3-4807-8b09-2a5699431e14"
        },
        {
            "email": "jameskshin2000@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "James Shin",
            "has_profile_photo": false,
            "user_id": "b4e78c21-8dea-4c27-99a9-c67c719bafa6"
        },
        {
            "email": "jerrynjodyg@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jody Granger",
            "has_profile_photo": false,
            "user_id": "b4ec4397-16ba-4db1-acaf-4235ccbddcd9"
        },
        {
            "email": "mullen.a.rachel@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rachel Mullen",
            "has_profile_photo": false,
            "user_id": "b5bda0e8-fa09-4b5e-be62-72f229ad4037"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Matt Hughes Total Pool Service Dannielle Milliken",
            "has_profile_photo": false,
            "user_id": "b6fab666-b67b-448c-8c2d-c66ef12f8705"
        },
        {
            "email": "sobh.dmd19@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Khouloud Sobh",
            "has_profile_photo": false,
            "user_id": "b7493001-46d0-4aee-8f04-4ab2414db7ca"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sharon Lot 35 Cook no LP",
            "has_profile_photo": false,
            "user_id": "b828c350-f928-4039-849b-d136db15bb8f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Irma Santiago cleaning lady Edye Bagheri",
            "has_profile_photo": false,
            "user_id": "b8cdfa28-6616-401d-a2c8-08d3043ed3a6"
        },
        {
            "email": "cherilyn@crcge.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cherilyn CRC Engineering",
            "has_profile_photo": false,
            "user_id": "b91ae144-cde3-4242-ab46-baf5e1d229e8"
        },
        {
            "email": "jfornaca619@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Joel Fornaca",
            "has_profile_photo": false,
            "user_id": "b97e4a35-bc2a-49ea-9522-266a9227c840"
        },
        {
            "email": "jason@mauih2o.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jason Bergstrom",
            "has_profile_photo": false,
            "user_id": "b994820d-871b-426f-99ff-f8c9785253c1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jennifer Thompson",
            "has_profile_photo": false,
            "user_id": "bb0ab852-db72-4967-9fa1-52c7e171018a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Beverly Ramirez",
            "has_profile_photo": false,
            "user_id": "bb4f1417-a1b4-40f9-8b04-38e3c0d17750"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Peter Wallace",
            "has_profile_photo": false,
            "user_id": "bb5bf103-19e5-4140-a422-e28b555dd772"
        },
        {
            "email": "b.lostetter@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Brittany Lostetter",
            "has_profile_photo": false,
            "user_id": "bb61d324-befa-4bc9-93ae-dee69e7fc250"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ann Peabody",
            "has_profile_photo": false,
            "user_id": "bb63c062-1799-4515-bc93-3c2d0924dbaa"
        },
        {
            "email": "samf715@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sami Faqih",
            "has_profile_photo": false,
            "user_id": "bbed6f1d-0740-45c0-86ae-36ac5263f3cd"
        },
        {
            "email": "jodiwilliams829@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jodi Williams",
            "has_profile_photo": false,
            "user_id": "bc3aaf30-2cc6-433d-9f68-1cab9758abd1"
        },
        {
            "email": "rgonzalez@starsinfantprogram.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rosa Gonzalez",
            "has_profile_photo": false,
            "user_id": "bc751892-9d2f-4837-8b3f-f0d9a394743f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Clear Expectations Pool Tristan Karla Hernandaz",
            "has_profile_photo": false,
            "user_id": "bcdef1b0-c024-45a5-8bc7-173fc830db47"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "jessica Lopez caregiver Thompson",
            "has_profile_photo": false,
            "user_id": "bce56d6d-0aa6-42ac-90c2-6f81af44270d"
        },
        {
            "email": "soianessa@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Stacey Iannessa",
            "has_profile_photo": false,
            "user_id": "be39ec11-a1ab-480b-a7c8-9b4ad2d1a378"
        },
        {
            "email": "ering1963@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Erin Garcia",
            "has_profile_photo": false,
            "user_id": "bee2dcae-7bbc-4d21-8ea7-a07b735456e0"
        },
        {
            "email": "ejnjho@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jeremy Howard",
            "has_profile_photo": false,
            "user_id": "bef1cf93-1c0e-4754-9a90-1fc2541b2fb9"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ethan Raikoglo",
            "has_profile_photo": false,
            "user_id": "bf1c16a5-b8c4-4b25-a858-c38e746fadf5"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Connor McManigal",
            "has_profile_photo": false,
            "user_id": "bf3c7281-6911-40b0-8d99-4fad6c4eecd5"
        },
        {
            "email": "Barryshadid@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Barry Shadid",
            "has_profile_photo": false,
            "user_id": "bfbb3886-24c8-46eb-97d2-7f485fb8066a"
        },
        {
            "email": "dianegreavesrn@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Diane Greaves",
            "has_profile_photo": false,
            "user_id": "c0ffb5b1-65a5-4cd5-95f1-c23cdec3388b"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jose Arcstone KELLEY SCUTELNICU",
            "has_profile_photo": false,
            "user_id": "c13b9dcf-8c43-4efe-8480-394c9f757f5c"
        },
        {
            "email": "jjakdavitt@aol.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Karla Davitt",
            "has_profile_photo": false,
            "user_id": "c147017b-be50-47c6-99b8-83267ba0cff0"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "San Diego Poolman Colleen Lister",
            "has_profile_photo": false,
            "user_id": "c1b0bf8a-e537-4675-b700-6bb5c28d93ae"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Community glass Bob Stall Arleen Liveky",
            "has_profile_photo": false,
            "user_id": "c1c4d56b-30d0-4e19-a78c-ac3a9bf4287c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Clara cleaning Pat Tanabe",
            "has_profile_photo": false,
            "user_id": "c2a5f99c-b869-4f3b-90f1-3cfa59e4cbd2"
        },
        {
            "email": "allegramartins@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Allegra Martins",
            "has_profile_photo": false,
            "user_id": "c314928e-33cf-470d-91e6-d423d7346b3a"
        },
        {
            "email": "michelle.minkoff@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Michelle Minkoff",
            "has_profile_photo": false,
            "user_id": "c3dfe5df-b7f6-4278-89ee-df59d5c6c0ef"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Andrew AVR Pest Control John DelMastro",
            "has_profile_photo": false,
            "user_id": "c483ce65-8b6e-4ace-b10b-fa9b20acb6ef"
        },
        {
            "email": "support+jacobwasvick+1727885660@verkada.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Verkada Support",
            "has_profile_photo": false,
            "user_id": "c511d04a-0e55-44f9-a8f5-39013c3668a9"
        },
        {
            "email": "thirdthorn@sbcglobal.net",
            "employee_id": "",
            "external_id": "",
            "full_name": "Roberto Lozano",
            "has_profile_photo": false,
            "user_id": "c57ce4f0-152a-4337-8de7-769f1e535f67"
        },
        {
            "email": "getse@vintagecellars.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Paola Noel",
            "has_profile_photo": false,
            "user_id": "c5822ed4-2047-4e64-acc6-d8cc15877b88"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Pool guy Matt Ben Errez",
            "has_profile_photo": false,
            "user_id": "c6c661f4-4bd6-4e0e-aedd-10aff7f1ee40"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Eduardo Albarran",
            "has_profile_photo": false,
            "user_id": "c78948bd-1b20-47e2-9bb4-6f886f937529"
        },
        {
            "email": "natasha_bailey@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Natasha Sawh",
            "has_profile_photo": false,
            "user_id": "c85717d8-ad91-4587-9592-64687e2146f7"
        },
        {
            "email": "eborg760@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Eric Borg",
            "has_profile_photo": false,
            "user_id": "c92ec9b2-bd0d-4589-9897-4b59064497ea"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Daughter Honz",
            "has_profile_photo": false,
            "user_id": "ca309df7-f172-487e-815c-a66f073bf2fc"
        },
        {
            "email": "jorge@greensidegardens.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jorge HOA Landscaper Greenside Gardens",
            "has_profile_photo": false,
            "user_id": "ca6daddc-2dba-435f-bba1-64cf349f7957"
        },
        {
            "email": "cccook707@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Craig Lot 34 Cook no LP",
            "has_profile_photo": false,
            "user_id": "caf62fff-2415-479f-be11-de2ce634e435"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "DHL Delivery",
            "has_profile_photo": false,
            "user_id": "cb01b66b-8d16-4008-a63d-3e80ecd88943"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Brian Concannon",
            "has_profile_photo": false,
            "user_id": "cb58f8ae-4833-4cbb-844c-725703a4f18a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sheriff Volunteer Patrol",
            "has_profile_photo": false,
            "user_id": "cbcaa49c-2093-42c0-acde-fcedcd51507a"
        },
        {
            "email": "williamdebow@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "William DeBow",
            "has_profile_photo": false,
            "user_id": "cbd01cea-87b2-45b0-9328-b70e1b2cd0a9"
        },
        {
            "email": "gretchenmacknight@cox.net",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gretchen Macknight",
            "has_profile_photo": false,
            "user_id": "cbe2fba1-2e46-49a5-899b-3afdcb0c5b9d"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Hui Li",
            "has_profile_photo": false,
            "user_id": "cd2eb1e4-2133-4769-b7ce-3da5b8059e3c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Patterson Pool Service Michael Franklin",
            "has_profile_photo": false,
            "user_id": "cd625ae4-6d35-48ef-baba-8164a673bbd2"
        },
        {
            "email": "jakenewberry@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jake Newberry",
            "has_profile_photo": false,
            "user_id": "ce097919-a064-4fdc-9b0d-ccbcb0d092a6"
        },
        {
            "email": "nicole@themontemurogroup.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Nicole Montemuro",
            "has_profile_photo": false,
            "user_id": "ce510716-b5db-4761-8ff2-09cf90e697c1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Steve Lot 3 Concannon",
            "has_profile_photo": false,
            "user_id": "ceaefe5b-2a75-47b7-8620-22b9650dd2f5"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Bryan King CRC Engineering",
            "has_profile_photo": false,
            "user_id": "cebc5067-492c-4f98-aa90-5fe06c488019"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ben Errez",
            "has_profile_photo": false,
            "user_id": "cf0be88b-d308-4d8a-9701-68b0026bb064"
        },
        {
            "email": "abby.ramos27@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Abby Ramos",
            "has_profile_photo": false,
            "user_id": "d025bccf-1369-4197-827c-1d13c9306163"
        },
        {
            "email": "jtdinucci@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Wife Deceased",
            "has_profile_photo": false,
            "user_id": "d0575e76-405e-483e-93c6-ba0507b47928"
        },
        {
            "email": "zamanm@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mohammad Molla",
            "has_profile_photo": false,
            "user_id": "d058f70c-7629-4c49-82c4-3b661e0b8378"
        },
        {
            "email": "tahirysumaya@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sumaya Tahiry",
            "has_profile_photo": false,
            "user_id": "d0832aa9-99fd-428c-88c6-d4dbd73d567c"
        },
        {
            "email": "joaquinanand@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Joaquin Anand",
            "has_profile_photo": false,
            "user_id": "d143cd52-189f-4f4c-bc04-eb66f295e776"
        },
        {
            "email": "mullen.tim@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Tim Mullen",
            "has_profile_photo": false,
            "user_id": "d14b2e59-8523-4729-b275-3ae3264aacac"
        },
        {
            "email": "teamtlc@live.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Thomas Chung",
            "has_profile_photo": false,
            "user_id": "d1aec312-99db-40a1-88f3-5d89a514d9ba"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rosa Montes David Garcia",
            "has_profile_photo": false,
            "user_id": "d1f64e2d-d541-4713-ab7f-702b59b7dd33"
        },
        {
            "email": "finance@golden-monkey.me",
            "employee_id": "",
            "external_id": "",
            "full_name": "Marc Wrona",
            "has_profile_photo": false,
            "user_id": "d259648d-3d6e-4e5f-b4af-851c9cf67a34"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Craig Webster",
            "has_profile_photo": false,
            "user_id": "d34ca8f8-4772-470c-a507-d4f38abea7a9"
        },
        {
            "email": "brivo@corsecurity.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "COR Security",
            "has_profile_photo": false,
            "user_id": "d34d7b2e-b7d8-469a-b4fb-f30051182033"
        },
        {
            "email": "lcolletti813@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "101 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "d37ff1e0-f3c0-4069-95d4-eb18c6b84e78"
        },
        {
            "email": "bdstepien@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Barbara Stepien",
            "has_profile_photo": false,
            "user_id": "d3edcb24-7a79-4215-9b6c-7003e7c1c23f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jerry Rolon",
            "has_profile_photo": false,
            "user_id": "d44286c5-7123-4280-a54d-3bba564b35a8"
        },
        {
            "email": "barbaravictor444@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Barbara Victor",
            "has_profile_photo": false,
            "user_id": "d4dfedb1-f64c-43e4-aeb6-cf7ae6de5b1f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "6767 Crystal Ridge Drive",
            "has_profile_photo": false,
            "user_id": "d57563b3-d165-4f50-8004-ce933cf413c1"
        },
        {
            "email": "meghanmilliken4@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Meghan Milliken",
            "has_profile_photo": false,
            "user_id": "d5cfdfb8-74d8-4999-900a-bac0407374ad"
        },
        {
            "email": "andrewdemaria1@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Andrew DeMaria",
            "has_profile_photo": false,
            "user_id": "d5df5087-c492-4f28-bc2b-1bb25e125756"
        },
        {
            "email": "eddielain@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Eddie Lain Blackman",
            "has_profile_photo": false,
            "user_id": "d620c4e5-cbd5-4163-ad3f-de215dddd365"
        },
        {
            "email": "travelfool62@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Suzanne Snyder",
            "has_profile_photo": false,
            "user_id": "d654b3f2-462c-4cfd-ac10-8c6d9953c27e"
        },
        {
            "email": "johnmarkmorris@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mark Morris",
            "has_profile_photo": false,
            "user_id": "d6b636d0-dc78-4560-b70e-595d9ca0c728"
        },
        {
            "email": "cadena680@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Alejandra Cadena-Perez",
            "has_profile_photo": false,
            "user_id": "d70f01a3-8d69-4091-9f09-6ce0e21e5191"
        },
        {
            "email": "edye57.bagheri@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Edye Bagher",
            "has_profile_photo": false,
            "user_id": "d7940fae-2754-4af7-94f7-2732a4d6d4da"
        },
        {
            "email": "jakeroth.23@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jake Roth",
            "has_profile_photo": false,
            "user_id": "d7bd7cb8-f38e-4711-bee6-7fa07d16d9be"
        },
        {
            "email": "danielaperry2015@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Daniela Perry",
            "has_profile_photo": false,
            "user_id": "d8b2844c-984a-42ca-ab9a-97797a8c8d28"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cleaner Ben Errez",
            "has_profile_photo": false,
            "user_id": "d938b497-81ff-4f09-97a6-3c2e3807ca34"
        },
        {
            "email": "support+jacobwasvick+1728319229@verkada.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Verkada Support",
            "has_profile_photo": false,
            "user_id": "d9479a22-96b4-42ee-8550-32817c389cb3"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Victor Bartolo Landscape Dawn Korinek",
            "has_profile_photo": false,
            "user_id": "d9d8eeb2-6cd4-4bed-bd80-4f5fef7034bd"
        },
        {
            "email": "megafurg@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Meghan Furgerson",
            "has_profile_photo": false,
            "user_id": "d9f80a7c-9926-4055-8b26-1e167d632847"
        },
        {
            "email": "emailingcindy@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cindy Richardson",
            "has_profile_photo": false,
            "user_id": "dade27c8-1595-439c-b706-8ef5e9da6847"
        },
        {
            "email": "primarlyn@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Primarlyn Anand",
            "has_profile_photo": false,
            "user_id": "dc3d3d00-a53b-4fa2-bac5-39603e93fd2c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rob Carpenter 2",
            "has_profile_photo": false,
            "user_id": "dcf29ff1-53c9-49e6-8e25-fe56905f24f3"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Nicole Montemuro",
            "has_profile_photo": false,
            "user_id": "dd071275-a63e-4671-b7a8-29fb72c6138f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Alina Thompson",
            "has_profile_photo": false,
            "user_id": "dd93eeaf-e4e5-4a46-b6c3-9289536daa07"
        },
        {
            "email": "trish@chezbasinet.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Patricia Basinet",
            "has_profile_photo": false,
            "user_id": "df5be0fa-f3ce-4262-8183-882a064420fc"
        },
        {
            "email": "pfurgie@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Paula Furgerson",
            "has_profile_photo": false,
            "user_id": "e029f545-2ef1-4a31-8633-f21f4b87d7d6"
        },
        {
            "email": "david@supercoolcreative.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "David Murdico",
            "has_profile_photo": false,
            "user_id": "e0f15752-45ca-49a5-b5a7-4034d96ceed8"
        },
        {
            "email": "arleen.gwa@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Arleen Lively",
            "has_profile_photo": false,
            "user_id": "e1a5f5a2-d51b-4328-bb14-8467dda30faf"
        },
        {
            "email": "asiaweleski@mossy.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Anthony Siaweleski",
            "has_profile_photo": false,
            "user_id": "e3088df6-23a0-40ac-9090-64dbeba06968"
        },
        {
            "email": "kldeborbo@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Kelly Desorbo",
            "has_profile_photo": false,
            "user_id": "e4870af0-5225-451a-b0fb-6a82e00dfe55"
        },
        {
            "email": "andyetemadi@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Andy Etemadi",
            "has_profile_photo": false,
            "user_id": "e4c1a370-43d9-4a09-8804-2b64113cf57d"
        },
        {
            "email": "arniecarzzz@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Arnold Carter",
            "has_profile_photo": false,
            "user_id": "e4d15971-fc84-4f32-b8cd-bd7fcbe7d0f9"
        },
        {
            "email": "jakerex@aol.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jennie Lot 3 Concannon",
            "has_profile_photo": false,
            "user_id": "e4d6d90a-a81c-4d3f-bcff-501b541830dc"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ron Schiller CRC Engineering",
            "has_profile_photo": false,
            "user_id": "e51996b7-ecc2-460f-9461-9d50aa40fd6a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Craig Cook",
            "has_profile_photo": false,
            "user_id": "e51c3983-0a00-4af9-9b19-7c891bca1eaa"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "26 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "e51e5983-56bb-45c3-82af-20ccab0d3b50"
        },
        {
            "email": "firatozkan@usa.net",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mehmet Firat Ozkan",
            "has_profile_photo": false,
            "user_id": "e58272ee-bcc7-4562-aee7-f9b698d911b1"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock no activity Heavens",
            "has_profile_photo": false,
            "user_id": "e5a768e3-8f2f-4ba2-b7fd-1717ef3bad47"
        },
        {
            "email": "srmontanoviva@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Francisco Cervantes",
            "has_profile_photo": false,
            "user_id": "e5cca05c-5a44-4c75-96f3-2d3893e1bd02"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Dustin Precision Equatics Kelley Scutelnicu",
            "has_profile_photo": false,
            "user_id": "e637f120-6fb5-45ce-b323-c2b5ea6ad38f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "LCL 9770 Jennifer Best-Martin",
            "has_profile_photo": false,
            "user_id": "e82fc40c-bce0-477d-84b6-7d9635b00f3a"
        },
        {
            "email": "doreneshadid@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Dorene Shadid",
            "has_profile_photo": false,
            "user_id": "e8627aae-87d2-4879-8518-e4fc967960e9"
        },
        {
            "email": "skhanijow@aol.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sheila Khanijow",
            "has_profile_photo": false,
            "user_id": "e8af8acd-2e8f-4288-ad0f-bed5fff96475"
        },
        {
            "email": "cs7477@att.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Cristina Siaweleski",
            "has_profile_photo": false,
            "user_id": "e9547fc8-1e2e-4f17-9ee2-df69d257527a"
        },
        {
            "email": "tomgraves61@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Tom Graves",
            "has_profile_photo": false,
            "user_id": "e9962354-1db0-4bdc-a771-158a092f4354"
        },
        {
            "email": "alnajjarrawan@hotmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rawan Alnajjar",
            "has_profile_photo": false,
            "user_id": "ea22fbba-569c-4bd4-8a18-0d1b8fccfe5a"
        },
        {
            "email": "jsanthoff@orioncable.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "John Santhoff Orion Cable",
            "has_profile_photo": false,
            "user_id": "ea8f74fe-cc83-49e6-9012-701aa9253268"
        },
        {
            "email": "cmkrissoff@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Christine Krissoff",
            "has_profile_photo": false,
            "user_id": "eafbd2d6-8ffb-426a-b211-e517f48d6d81"
        },
        {
            "email": "jimfornaca@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jim Fornaca",
            "has_profile_photo": false,
            "user_id": "eb0a516a-00db-41e5-af26-7a45a7e82983"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Scott Klee handyman Arnie Carter",
            "has_profile_photo": false,
            "user_id": "eb22fd4d-69c4-4ef4-863e-d9d99a845cec"
        },
        {
            "email": "markpalmer187@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mark Palmer",
            "has_profile_photo": false,
            "user_id": "eb4ba715-ded8-493d-8620-dcd7882d428f"
        },
        {
            "email": "otoupet@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Olivier Toupet",
            "has_profile_photo": false,
            "user_id": "eb855382-f6ee-4295-af95-c252da057a3f"
        },
        {
            "email": "Exp2884@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "54 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "ebb5bf11-0f20-4904-8a27-ffbab6908eaf"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "6767 Crystal Ridge Drive",
            "has_profile_photo": false,
            "user_id": "ebc9feaf-0d2f-4a29-b76b-13d3b39145f5"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Romero Paint Mrs. Garcia Arleen Lively",
            "has_profile_photo": false,
            "user_id": "ebe5987c-6724-4199-b349-0963d60e52d3"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Metal Works Keith Pospychale Lively",
            "has_profile_photo": false,
            "user_id": "ec2dfb76-28fe-4410-a4e5-c96684070a05"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mikol Bee removal & Pest control Daniel Perry",
            "has_profile_photo": false,
            "user_id": "ec9fd3a0-4d7d-4e82-815f-f6ca71df2995"
        },
        {
            "email": "j.lostetter02@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jacob Lostetter",
            "has_profile_photo": false,
            "user_id": "ed0b5e86-ee29-4fa6-8698-994e9ab0f7c4"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gardener Milliken",
            "has_profile_photo": false,
            "user_id": "ed2cfbbb-9f20-4e7a-bdaa-7b437df1f4aa"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Trey CRC Engineering",
            "has_profile_photo": false,
            "user_id": "ed58c8e7-e6e9-4154-9605-4eb9cc6a2146"
        },
        {
            "email": "mramos@starsinfantprogram.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mark Ramos",
            "has_profile_photo": false,
            "user_id": "eddc7310-8697-4a71-be56-db5cd1a4a1ca"
        },
        {
            "email": "lynn18_june@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Madelyn Santiago",
            "has_profile_photo": false,
            "user_id": "ede7a1e1-e396-46f7-8292-b32881852b68"
        },
        {
            "email": "sanakubba@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Sana Kubba",
            "has_profile_photo": false,
            "user_id": "edfc140d-74a5-45a2-91c9-f670120dcbbc"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "guest Dawn Fuller",
            "has_profile_photo": false,
            "user_id": "eeb5b929-0e2e-48b2-b9e8-4be371f69634"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Eunjoo Jang Howard",
            "has_profile_photo": false,
            "user_id": "eeedc86f-ad1b-409f-a078-7a5248b3e5c4"
        },
        {
            "email": "gschafer@aboutcis.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gerald Schafer",
            "has_profile_photo": false,
            "user_id": "eef846b2-e9a6-4c3f-a145-5ab1765c4605"
        },
        {
            "email": "melaniet039@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Melanie Thompson",
            "has_profile_photo": false,
            "user_id": "ef1cdf22-2cba-416a-80d3-310a32dad72e"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock no activity Heavens",
            "has_profile_photo": false,
            "user_id": "ef5bd3ad-5dc6-429e-a40d-db0f4473fc2a"
        },
        {
            "email": "hlamanda9988@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Hui Li",
            "has_profile_photo": false,
            "user_id": "ef7929d7-b3fc-413d-921e-7eead7070e84"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rosa Montes House Cleaning Helen Wallace",
            "has_profile_photo": false,
            "user_id": "f026cc67-210c-4709-91a9-abdb143e773d"
        },
        {
            "email": "jlu_sd@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jian Lu",
            "has_profile_photo": false,
            "user_id": "f04eaf80-a906-442f-aaab-9f2162f9f4a0"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "29432 Welk Highland Drive",
            "has_profile_photo": false,
            "user_id": "f06d8092-67e2-4aa1-a571-b22722dc9fd6"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "54 Meadow Glen Way West",
            "has_profile_photo": false,
            "user_id": "f08236f2-e2ea-458b-bba6-9cd863355ab8"
        },
        {
            "email": "ulamirjan@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ula Mirjan Trust",
            "has_profile_photo": false,
            "user_id": "f13eafce-a042-4074-8e10-0bc4366f659e"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Trinidad Mesa Union Tribune delivery",
            "has_profile_photo": false,
            "user_id": "f1f95fca-4844-4c11-b89a-776d89b15566"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Lloyd Pest Control Jim Fornaca",
            "has_profile_photo": false,
            "user_id": "f218f438-ad1f-4af2-bc7b-7478645f5a18"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Art's Marble Antonio Solis Arleen Lively",
            "has_profile_photo": false,
            "user_id": "f2387088-77af-4a1a-8ccc-98a25cb3f1dd"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Craig Lot 35 Cook no LP",
            "has_profile_photo": false,
            "user_id": "f292a0ef-a9d2-4f97-b1b2-bd8dfef0a60b"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "House cleaner Jeanne DeMeules",
            "has_profile_photo": false,
            "user_id": "f2eebc61-7d94-4a97-9ce4-68fc315c42a6"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ismael Reyes CRC Engineering",
            "has_profile_photo": false,
            "user_id": "f44a9078-558c-48da-87a6-33491e0e5fa1"
        },
        {
            "email": "Austin.Scutelnicu@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Austin Scutelnicu",
            "has_profile_photo": false,
            "user_id": "f4c8279f-2b4b-4887-b6a8-efb07f5404e8"
        },
        {
            "email": "halcyonsandiego@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Richard Ring",
            "has_profile_photo": false,
            "user_id": "f53d30a3-37a1-46db-b9cd-6bbff42249f9"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "weekend visitor Reardon",
            "has_profile_photo": false,
            "user_id": "f5b26bb8-64ad-4c96-83d1-ffe8d51a4b07"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Chris Johnson",
            "has_profile_photo": false,
            "user_id": "f61a1e47-8a18-48b9-94b2-15f490a71ecb"
        },
        {
            "email": "hle0831@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Huong T Le",
            "has_profile_photo": false,
            "user_id": "f63a333e-3b61-4565-a55b-76461de28912"
        },
        {
            "email": "edenlbergstrom@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Eden Bergstrom",
            "has_profile_photo": false,
            "user_id": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c"
        },
        {
            "email": "daniel.minkoff@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Daniel Minkoff",
            "has_profile_photo": false,
            "user_id": "f67b8ed1-6649-4788-894c-fa857f926118"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "RimRock #2 Heavens",
            "has_profile_photo": false,
            "user_id": "f6a70571-8921-42b6-8c37-11c58d886e37"
        },
        {
            "email": "858ishome@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Suresh Patibandla",
            "has_profile_photo": false,
            "user_id": "f6ee79f1-01a9-4045-b4f5-17d1167a7519"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Gabriel Gardeners Adam Levy",
            "has_profile_photo": false,
            "user_id": "f756631f-bce5-4166-854e-61e30c1d990a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Ammar Farah",
            "has_profile_photo": false,
            "user_id": "f79cad78-c54d-4825-ae80-57f2cbf2050a"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Greg Schaefer caregiver Melanie Thompson",
            "has_profile_photo": false,
            "user_id": "f7aff736-d467-4071-ae83-16292071c50c"
        },
        {
            "email": "itstabusushi92078@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Rouba Staites",
            "has_profile_photo": false,
            "user_id": "f7c1ba71-c511-4f8e-ac83-668e4c971aee"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "LCL 9778 Dawn Fuller",
            "has_profile_photo": false,
            "user_id": "f7e352b1-a80d-4957-ba31-9f86f43b5b9f"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "CRD 9785 Karla Hernandaz",
            "has_profile_photo": false,
            "user_id": "f8d3873c-65b8-4ed0-b7ec-9ae894b527cc"
        },
        {
            "email": "raschelakloos@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Raschel Kloos",
            "has_profile_photo": false,
            "user_id": "f8e1901b-e4c8-4a98-a414-f3b1f4f67121"
        },
        {
            "email": "lupita_madrigal1973@icloud.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Lupita Madrigal caretaker Kang",
            "has_profile_photo": false,
            "user_id": "f93c2d68-f933-4742-a5be-b2557c11e81e"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Steven Hanlon",
            "has_profile_photo": false,
            "user_id": "f956b96d-3846-4dce-9c93-b88000cca812"
        },
        {
            "email": "juliet_navas@yahoo.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Juliet Navas",
            "has_profile_photo": false,
            "user_id": "f9bdc32f-8ad7-47a4-b8f7-eaaa169e3273"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Romero Paint Esli Garcia Arleen Lively",
            "has_profile_photo": false,
            "user_id": "f9e3558e-e764-4fbd-ac1a-62b043a44729"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Mark Gregson Lot 65 #2",
            "has_profile_photo": false,
            "user_id": "fa70e220-908f-47c6-985d-8a036f0b1b25"
        },
        {
            "email": "fred@crcge.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Fred CRC Engineering",
            "has_profile_photo": false,
            "user_id": "fb39a5a3-5fe4-49da-9924-74befab3ce40"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Orkin Pest Control Adam Levy",
            "has_profile_photo": false,
            "user_id": "fba51829-a61d-4d41-9b1b-67b14c1058aa"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Chelsea Shaw",
            "has_profile_photo": false,
            "user_id": "fbec7b2f-64a0-4e27-a0d2-84253bae6aa3"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Phil Gates Pool Serv Helen Wallace",
            "has_profile_photo": false,
            "user_id": "fc718f67-9df3-4416-b7be-c9fefc5a077c"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jaime Rivera Gardener Molla",
            "has_profile_photo": false,
            "user_id": "fcc4430c-d876-4dff-aa17-af2036b3a6b7"
        },
        {
            "email": "michael@martinsohana.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Michael Martins",
            "has_profile_photo": false,
            "user_id": "fd12b74b-663c-42c0-a4f4-c5b4d7b03dd5"
        },
        {
            "email": "maingatejason8@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jason MainGate",
            "has_profile_photo": false,
            "user_id": "fd1eefaa-a15e-46d0-8d49-cff48775543a"
        },
        {
            "email": "batoul.tahiry@brightstarcare.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Batoul Tahiry",
            "has_profile_photo": false,
            "user_id": "fe3f78b7-aece-46df-bcc8-05ff557c8300"
        },
        {
            "email": "jfbn.vee@gmail.com",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jonathan Villariasa",
            "has_profile_photo": false,
            "user_id": "fe72eaf5-31f7-4763-a38b-343e6d0b7209"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Jillian Cardona",
            "has_profile_photo": false,
            "user_id": "feb74a54-e83d-40cf-a231-79dc4244380e"
        },
        {
            "email": "",
            "employee_id": "",
            "external_id": "",
            "full_name": "Amazon Regular Van",
            "has_profile_photo": false,
            "user_id": "ff888493-3314-4d2e-bb3f-16899eef7f8c"
        }
    ]
}
2025-04-26 22:13:49,850 - __main__ - INFO - Successfully retrieved access users list (first page). Found 645 users on this page.
2025-04-26 22:13:49,850 - src_helix.api_utils - INFO - Generated JSON template: src_helix/api-json/test_users_list_api.json
PASS: Access Users List

--------------------------------------------------------------------------------
Running Test: Access User Details
Script: test_user_details_api.py
--------------------------------------------------------------------------------
  -> Fetching user list to select first user...
  -> Selected first user: Cabinet Install Michael Danino Arleen Lively (ID: 00439...)
--------------------------------------------------------------------------------
Running: python -m src_helix.test_user_details_api --log_level INFO --user_id 00439f7b-74ac-4a3f-b0f2-5e6500fae55f
--------------------------------------------------------------------------------
2025-04-26 22:13:52,515 - __main__ - INFO - Successfully retrieved API token: v2_f0500c8...
2025-04-26 22:13:52,515 - __main__ - INFO - Attempting to fetch details for user ID: 00439f7b-74ac-4a3f-b0f2-5e6500fae55f...

Detail information for user ID: 00439f7b-74ac-4a3f-b0f2-5e6500fae55f

--- Access User Details API Response (User ID: 00439f7b-74ac-4a3f-b0f2-5e6500fae55f) ---
{
    "access_groups": [
        {
            "group_id": "28fdd2c0-b565-4abb-8da3-1fb7c5f08116",
            "name": "2. Household Vendors"
        }
    ],
    "ble_unlock": true,
    "cards": [],
    "end_date": "1743880833",
    "entry_code": "",
    "has_profile_photo": false,
    "license_plates": [
        {
            "active": true,
            "license_plate_number": "8TMR679",
            "name": "8TMR679"
        }
    ],
    "mfa_codes": [],
    "remote_unlock": false,
    "start_date": "1733343658",
    "user_id": "00439f7b-74ac-4a3f-b0f2-5e6500fae55f"
}
2025-04-26 22:13:53,246 - __main__ - INFO - Successfully retrieved details for user ID: 00439f7b-74ac-4a3f-b0f2-5e6500fae55f
2025-04-26 22:13:53,247 - src_helix.api_utils - INFO - Generated JSON template: src_helix/api-json/test_user_details_api.json
PASS: Access User Details

--------------------------------------------------------------------------------
Running Test: Camera Notifications
Script: test_notifications_api.py
--------------------------------------------------------------------------------
  -> Using default history_days=1
--------------------------------------------------------------------------------
Running: python -m src_helix.test_notifications_api --log_level INFO --history_days 1
--------------------------------------------------------------------------------
2025-04-26 22:13:54,269 - __main__ - INFO - Successfully retrieved API token: v2_ca4e9dd...
2025-04-26 22:13:54,270 - __main__ - INFO - Querying notifications for the last 1 days (from 2025-04-25 22:13:54 to 2025-04-26 22:13:54)
2025-04-26 22:13:54,270 - __main__ - INFO - Attempting to fetch notifications from /cameras/v1/alerts

--- Notifications API Response from /cameras/v1/alerts ---
{
    "next_page_token": null,
    "notifications": [
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745718362,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745718362/?duration=86400&initialVideoTime=1745718362000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745716663,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745716663/?duration=86400&initialVideoTime=1745716663000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745716043,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745716043/?duration=86400&initialVideoTime=1745716043000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745715641,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745715641/?duration=86400&initialVideoTime=1745715641000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745711420,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745711420/?duration=86400&initialVideoTime=1745711420000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745711054,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745711054/?duration=86400&initialVideoTime=1745711054000"
        },
        {
            "camera_id": "ab34699a-038b-41b4-98b4-9d83055489b6",
            "created": 1745705977,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/ab34699a-038b-41b4-98b4-9d83055489b6/history/86400/1745705977/?duration=86400&initialVideoTime=1745705977000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745705853,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745705853/?duration=86400&initialVideoTime=1745705853000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745702516,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745702516/?duration=86400&initialVideoTime=1745702516000"
        },
        {
            "camera_id": "f9cd473f-3794-4bee-825c-d1ae60d8e791",
            "created": 1745702446,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/f9cd473f-3794-4bee-825c-d1ae60d8e791/history/86400/1745702446/?duration=86400&initialVideoTime=1745702446000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745701854,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745701854/?duration=86400&initialVideoTime=1745701854000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745701192,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745701192/?duration=86400&initialVideoTime=1745701192000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745698845,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745698845/?duration=86400&initialVideoTime=1745698845000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745698794,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745698794/?duration=86400&initialVideoTime=1745698794000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745695049,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745695049/?duration=86400&initialVideoTime=1745695049000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745694789,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745694789/?duration=86400&initialVideoTime=1745694789000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745694159,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745694159/?duration=86400&initialVideoTime=1745694159000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745694134,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745694134/?duration=86400&initialVideoTime=1745694134000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745693830,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745693830/?duration=86400&initialVideoTime=1745693830000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745693452,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745693452/?duration=86400&initialVideoTime=1745693452000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745693135,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745693135/?duration=86400&initialVideoTime=1745693135000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745692957,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745692957/?duration=86400&initialVideoTime=1745692957000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745692899,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745692899/?duration=86400&initialVideoTime=1745692899000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745691195,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745691195/?duration=86400&initialVideoTime=1745691195000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745690794,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745690794/?duration=86400&initialVideoTime=1745690794000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745689491,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745689491/?duration=86400&initialVideoTime=1745689491000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745687837,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745687837/?duration=86400&initialVideoTime=1745687837000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745686953,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745686953/?duration=86400&initialVideoTime=1745686953000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745686637,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745686637/?duration=86400&initialVideoTime=1745686637000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745679619,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745679619/?duration=86400&initialVideoTime=1745679619000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745679088,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745679088/?duration=86400&initialVideoTime=1745679088000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745661636,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745661636/?duration=86400&initialVideoTime=1745661636000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745644395,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745644395/?duration=86400&initialVideoTime=1745644395000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745640124,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745640124/?duration=86400&initialVideoTime=1745640124000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745639631,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745639631/?duration=86400&initialVideoTime=1745639631000"
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "created": 1745637593,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/d1e37446-ca48-4398-9243-49a99ea4bc80/history/86400/1745637593/?duration=86400&initialVideoTime=1745637593000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745636758,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745636758/?duration=86400&initialVideoTime=1745636758000"
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "created": 1745635303,
            "crowd_threshold": null,
            "image_url": null,
            "notification_type": "license_plate_of_interest",
            "objects": null,
            "person_label": null,
            "video_url": "https://command.verkada.com/cameras/2bc18656-7a1e-4612-b08a-4e1ae47364f0/history/86400/1745635303/?duration=86400&initialVideoTime=1745635303000"
        }
    ]
}
2025-04-26 22:13:54,804 - __main__ - INFO - Successfully retrieved 38 notifications.
2025-04-26 22:13:54,806 - src_helix.api_utils - INFO - Generated JSON template: src_helix/api-json/test_notifications_api.json
PASS: Camera Notifications

--------------------------------------------------------------------------------
Running Test: LPR Events (All LPR Cams)
Script: test_lpr_images_api_all_cameras.py
--------------------------------------------------------------------------------
  -> Using default history_hours=1
--------------------------------------------------------------------------------
Running: python -m src_helix.test_lpr_images_api_all_cameras --log_level INFO --history_hours 1
--------------------------------------------------------------------------------
2025-04-26 22:13:56,113 - __main__ - INFO - Successfully retrieved API token: v2_883bdeb...
2025-04-26 22:13:56,113 - __main__ - INFO - Querying LPR images for the last 1 hours (from 2025-04-26 21:13:56 to 2025-04-26 22:13:56)
2025-04-26 22:13:56,113 - src_helix.api_utils - INFO - Fetching all cameras...
2025-04-26 22:13:57,549 - src_helix.api_utils - INFO - Finished fetching all data from /cameras/v1/devices. Total items fetched: 10
2025-04-26 22:13:57,549 - src_helix.api_utils - INFO - Found 5 LPR-enabled cameras (filtered by 'License' in name).
2025-04-26 22:13:57,549 - __main__ - INFO - Fetching LPR images for camera: Mesa License Plate (ID: 2bc18656-7a1e-4612-b08a-4e1ae47364f0)
2025-04-26 22:14:02,563 - src_helix.api_utils - INFO - Finished fetching LPR images for camera 2bc18656-7a1e-4612-b08a-4e1ae47364f0. Total detections: 19
2025-04-26 22:14:02,563 - __main__ - INFO - Fetching LPR images for camera: Highland License Plate (ID: 8c219867-9e7a-40e1-b19d-020f7458558c)
2025-04-26 22:14:05,838 - src_helix.api_utils - INFO - Finished fetching LPR images for camera 8c219867-9e7a-40e1-b19d-020f7458558c. Total detections: 0
2025-04-26 22:14:05,838 - __main__ - INFO - Fetching LPR images for camera: Main Gate Exit License Plates (ID: ab34699a-038b-41b4-98b4-9d83055489b6)
2025-04-26 22:14:08,298 - src_helix.api_utils - INFO - Finished fetching LPR images for camera ab34699a-038b-41b4-98b4-9d83055489b6. Total detections: 0
2025-04-26 22:14:08,298 - __main__ - INFO - Fetching LPR images for camera: Mesa Exit License Plate (ID: d1e37446-ca48-4398-9243-49a99ea4bc80)
2025-04-26 22:14:12,291 - src_helix.api_utils - INFO - Finished fetching LPR images for camera d1e37446-ca48-4398-9243-49a99ea4bc80. Total detections: 7
2025-04-26 22:14:12,292 - __main__ - INFO - Fetching LPR images for camera: Main Gate License Plate  (ID: f9cd473f-3794-4bee-825c-d1ae60d8e791)
2025-04-26 22:14:17,517 - src_helix.api_utils - INFO - Finished fetching LPR images for camera f9cd473f-3794-4bee-825c-d1ae60d8e791. Total detections: 2
2025-04-26 22:14:17,517 - __main__ - INFO - Finished fetching LPR images from all LPR-enabled cameras. Total detections found: 28

--- LPR Detections Table ---
License Plate        | Gate (Camera Name)             | Day/Time            
----------------------------------------------------------------------------
1AE924V              | Mesa Exit License Plate        | 2025-04-26 21:17:43 
49TK39               | Mesa Exit License Plate        | 2025-04-26 21:18:21 
2717C1               | Mesa Exit License Plate        | 2025-04-26 21:18:31 
9DZD206              | Mesa License Plate             | 2025-04-26 21:23:19 
5VSL622              | Mesa License Plate             | 2025-04-26 21:23:27 
5FE1407              | Mesa License Plate             | 2025-04-26 21:25:37 
9MED309              | Mesa License Plate             | 2025-04-26 21:26:30 
5VSL622              | Mesa Exit License Plate        | 2025-04-26 21:28:17 
9BDP897              | Mesa License Plate             | 2025-04-26 21:28:32 
9LQX535              | Mesa Exit License Plate        | 2025-04-26 21:33:30 
7TNC370              | Mesa License Plate             | 2025-04-26 21:34:57 
4XFT021              | Main Gate License Plate        | 2025-04-26 21:37:18 
7PAL634              | Mesa Exit License Plate        | 2025-04-26 21:38:57 
9HYB970              | Mesa License Plate             | 2025-04-26 21:39:40 
9H0H039              | Mesa License Plate             | 2025-04-26 21:41:59 
9GBU330              | Mesa License Plate             | 2025-04-26 21:42:03 
17659H3              | Mesa License Plate             | 2025-04-26 21:42:38 
1AE924V              | Mesa License Plate             | 2025-04-26 21:46:02 
7PVS569              | Mesa Exit License Plate        | 2025-04-26 21:53:03 
7AYM395              | Mesa License Plate             | 2025-04-26 21:53:05 
1SKID0               | Mesa License Plate             | 2025-04-26 21:53:30 
7AYM395              | Mesa License Plate             | 2025-04-26 21:53:37 
9RLN223              | Mesa License Plate             | 2025-04-26 22:01:25 
6UAP937              | Mesa License Plate             | 2025-04-26 22:02:23 
9PBM125              | Mesa License Plate             | 2025-04-26 22:05:07 
9PXD257              | Mesa License Plate             | 2025-04-26 22:05:52 
6WTP420              | Mesa License Plate             | 2025-04-26 22:08:12 
9CBP500              | Main Gate License Plate        | 2025-04-26 22:10:48 
PASS: LPR Events (All LPR Cams)

--------------------------------------------------------------------------------
Running Test: LPR Events (LPOI Match)
Script: test_lpr_lpoi_match_api.py
--------------------------------------------------------------------------------
  -> Using default history_hours=1
--------------------------------------------------------------------------------
Running: python -m src_helix.test_lpr_lpoi_match_api --log_level INFO --history_hours 1
--------------------------------------------------------------------------------
2025-04-26 22:14:18,409 - __main__ - INFO - Successfully retrieved API token: v2_0acaad7...
2025-04-26 22:14:18,409 - __main__ - INFO - Fetching License Plates of Interest...
2025-04-26 22:14:18,409 - src_helix.api_utils - INFO - Fetching all License Plates of Interest (LPOI)...
2025-04-26 22:14:20,088 - src_helix.api_utils - INFO - Finished fetching all data from /cameras/v1/analytics/lpr/license_plate_of_interest. Total items fetched: 612
2025-04-26 22:14:20,088 - __main__ - INFO - Successfully retrieved 611 License Plates of Interest.
2025-04-26 22:14:20,088 - __main__ - INFO - Fetching LPR-enabled cameras...
2025-04-26 22:14:20,088 - src_helix.api_utils - INFO - Fetching all cameras...
2025-04-26 22:14:20,996 - src_helix.api_utils - INFO - Finished fetching all data from /cameras/v1/devices. Total items fetched: 10
2025-04-26 22:14:20,996 - src_helix.api_utils - INFO - Found 5 LPR-enabled cameras (filtered by 'License' in name).
2025-04-26 22:14:20,996 - __main__ - INFO - Querying ALL LPR images for the last 1 hours...
2025-04-26 22:14:20,996 - __main__ - INFO - Time range: 2025-04-26 21:14:20 to 2025-04-26 22:14:20
2025-04-26 22:14:20,996 - __main__ - INFO - Fetching LPR images for camera: Mesa License Plate (ID: 2bc18656-7a1e-4612-b08a-4e1ae47364f0)
2025-04-26 22:14:25,604 - src_helix.api_utils - INFO - Finished fetching LPR images for camera 2bc18656-7a1e-4612-b08a-4e1ae47364f0. Total detections: 19
2025-04-26 22:14:25,604 - __main__ - INFO - Fetching LPR images for camera: Highland License Plate (ID: 8c219867-9e7a-40e1-b19d-020f7458558c)
2025-04-26 22:14:28,266 - src_helix.api_utils - INFO - Finished fetching LPR images for camera 8c219867-9e7a-40e1-b19d-020f7458558c. Total detections: 0
2025-04-26 22:14:28,267 - __main__ - INFO - Fetching LPR images for camera: Main Gate Exit License Plates (ID: ab34699a-038b-41b4-98b4-9d83055489b6)
2025-04-26 22:14:30,932 - src_helix.api_utils - INFO - Finished fetching LPR images for camera ab34699a-038b-41b4-98b4-9d83055489b6. Total detections: 0
2025-04-26 22:14:30,932 - __main__ - INFO - Fetching LPR images for camera: Mesa Exit License Plate (ID: d1e37446-ca48-4398-9243-49a99ea4bc80)
2025-04-26 22:14:35,026 - src_helix.api_utils - INFO - Finished fetching LPR images for camera d1e37446-ca48-4398-9243-49a99ea4bc80. Total detections: 7
2025-04-26 22:14:35,026 - __main__ - INFO - Fetching LPR images for camera: Main Gate License Plate  (ID: f9cd473f-3794-4bee-825c-d1ae60d8e791)
2025-04-26 22:14:39,837 - src_helix.api_utils - INFO - Finished fetching LPR images for camera f9cd473f-3794-4bee-825c-d1ae60d8e791. Total detections: 2
2025-04-26 22:14:39,837 - __main__ - INFO - Finished fetching LPR images from all LPR-enabled cameras. Total detections fetched: 28.
2025-04-26 22:14:39,837 - __main__ - INFO - Filtering detections for LPOI matches...
2025-04-26 22:14:39,838 - __main__ - INFO - Found 9 LPOI matches.
----------------------------------------------------------------------------
| LPR Match to LPoI {611} ::::: 2025-04-26 21:14:20 to 2025-04-26 22:14:20 |
----------------------------------------------------------------------------
License Plate        | Gate (Camera Name)             | Day/Time            
----------------------------------------------------------------------------
1AE924V              | Mesa Exit License Plate        | 2025-04-26 21:17:43 
1AE924V              | Mesa License Plate             | 2025-04-26 21:46:02 
----------------------------------------------------------------------------
5FE1407              | Mesa License Plate             | 2025-04-26 21:25:37 
----------------------------------------------------------------------------
5VSL622              | Mesa License Plate             | 2025-04-26 21:23:27 
5VSL622              | Mesa Exit License Plate        | 2025-04-26 21:28:17 
----------------------------------------------------------------------------
7TNC370              | Mesa License Plate             | 2025-04-26 21:34:57 
----------------------------------------------------------------------------
9BDP897              | Mesa License Plate             | 2025-04-26 21:28:32 
----------------------------------------------------------------------------
9HYB970              | Mesa License Plate             | 2025-04-26 21:39:40 
----------------------------------------------------------------------------
9MED309              | Mesa License Plate             | 2025-04-26 21:26:30 
PASS: LPR Events (LPOI Match)

--------------------------------------------------------------------------------
Running Test: LPR Events (Non-LPOI)
Script: test_lpr_non_lpoi_report_api.py
--------------------------------------------------------------------------------
  -> Using default history_hours=1
--------------------------------------------------------------------------------
Running: python -m src_helix.test_lpr_non_lpoi_report_api --log_level INFO --history_hours 1
--------------------------------------------------------------------------------
2025-04-26 22:14:40,760 - __main__ - INFO - Successfully retrieved API token: v2_287959e...
2025-04-26 22:14:40,760 - __main__ - INFO - Fetching License Plates of Interest...
2025-04-26 22:14:40,760 - src_helix.api_utils - INFO - Fetching all License Plates of Interest (LPOI)...
2025-04-26 22:14:42,468 - src_helix.api_utils - INFO - Finished fetching all data from /cameras/v1/analytics/lpr/license_plate_of_interest. Total items fetched: 612
2025-04-26 22:14:42,469 - __main__ - INFO - Successfully retrieved 611 License Plates of Interest.
2025-04-26 22:14:42,469 - __main__ - INFO - Fetching LPR-enabled cameras...
2025-04-26 22:14:42,469 - src_helix.api_utils - INFO - Fetching all cameras...
2025-04-26 22:14:43,211 - src_helix.api_utils - INFO - Finished fetching all data from /cameras/v1/devices. Total items fetched: 10
2025-04-26 22:14:43,211 - src_helix.api_utils - INFO - Found 5 LPR-enabled cameras (filtered by 'License' in name).
2025-04-26 22:14:43,212 - __main__ - INFO - Querying LPR images for the last 1 hours...
2025-04-26 22:14:43,212 - __main__ - INFO - Time range: 2025-04-26 21:14:43 to 2025-04-26 22:14:43
2025-04-26 22:14:43,212 - __main__ - INFO - Fetching LPR images for camera: Mesa License Plate (ID: 2bc18656-7a1e-4612-b08a-4e1ae47364f0)
2025-04-26 22:14:47,825 - src_helix.api_utils - INFO - Finished fetching LPR images for camera 2bc18656-7a1e-4612-b08a-4e1ae47364f0. Total detections: 19
2025-04-26 22:14:47,825 - __main__ - INFO - Fetching LPR images for camera: Highland License Plate (ID: 8c219867-9e7a-40e1-b19d-020f7458558c)
2025-04-26 22:14:50,591 - src_helix.api_utils - INFO - Finished fetching LPR images for camera 8c219867-9e7a-40e1-b19d-020f7458558c. Total detections: 0
2025-04-26 22:14:50,591 - __main__ - INFO - Fetching LPR images for camera: Main Gate Exit License Plates (ID: ab34699a-038b-41b4-98b4-9d83055489b6)
2025-04-26 22:14:53,457 - src_helix.api_utils - INFO - Finished fetching LPR images for camera ab34699a-038b-41b4-98b4-9d83055489b6. Total detections: 0
2025-04-26 22:14:53,457 - __main__ - INFO - Fetching LPR images for camera: Mesa Exit License Plate (ID: d1e37446-ca48-4398-9243-49a99ea4bc80)
2025-04-26 22:14:57,551 - src_helix.api_utils - INFO - Finished fetching LPR images for camera d1e37446-ca48-4398-9243-49a99ea4bc80. Total detections: 7
2025-04-26 22:14:57,551 - __main__ - INFO - Fetching LPR images for camera: Main Gate License Plate  (ID: f9cd473f-3794-4bee-825c-d1ae60d8e791)
2025-04-26 22:15:01,240 - src_helix.api_utils - INFO - Finished fetching LPR images for camera f9cd473f-3794-4bee-825c-d1ae60d8e791. Total detections: 2
2025-04-26 22:15:01,240 - __main__ - INFO - Finished fetching LPR images from all LPR-enabled cameras. Total detections fetched: 28.
2025-04-26 22:15:01,240 - __main__ - INFO - Filtering detections for Non-LPOI...
2025-04-26 22:15:01,241 - __main__ - INFO - Found 19 Non-LPOI detections.
----------------------------------------------------------------------------
| LPR Detections (Non-LPoI) ::: 2025-04-26 21:14:43 to 2025-04-26 22:14:43 |
----------------------------------------------------------------------------
License Plate        | Gate (Camera Name)             | Day/Time            
----------------------------------------------------------------------------
17659H3              | Mesa License Plate             | 2025-04-26 21:42:38 
----------------------------------------------------------------------------
1SKID0               | Mesa License Plate             | 2025-04-26 21:53:30 
----------------------------------------------------------------------------
2717C1               | Mesa Exit License Plate        | 2025-04-26 21:18:31 
----------------------------------------------------------------------------
49TK39               | Mesa Exit License Plate        | 2025-04-26 21:18:21 
----------------------------------------------------------------------------
4XFT021              | Main Gate License Plate        | 2025-04-26 21:37:18 
----------------------------------------------------------------------------
6UAP937              | Mesa License Plate             | 2025-04-26 22:02:23 
----------------------------------------------------------------------------
6WTP420              | Mesa License Plate             | 2025-04-26 22:08:12 
----------------------------------------------------------------------------
7AYM395              | Mesa License Plate             | 2025-04-26 21:53:05 
7AYM395              | Mesa License Plate             | 2025-04-26 21:53:37 
----------------------------------------------------------------------------
7PAL634              | Mesa Exit License Plate        | 2025-04-26 21:38:57 
----------------------------------------------------------------------------
7PVS569              | Mesa Exit License Plate        | 2025-04-26 21:53:03 
----------------------------------------------------------------------------
9CBP500              | Main Gate License Plate        | 2025-04-26 22:10:48 
----------------------------------------------------------------------------
9DZD206              | Mesa License Plate             | 2025-04-26 21:23:19 
----------------------------------------------------------------------------
9GBU330              | Mesa License Plate             | 2025-04-26 21:42:03 
----------------------------------------------------------------------------
9H0H039              | Mesa License Plate             | 2025-04-26 21:41:59 
----------------------------------------------------------------------------
9LQX535              | Mesa Exit License Plate        | 2025-04-26 21:33:30 
----------------------------------------------------------------------------
9PBM125              | Mesa License Plate             | 2025-04-26 22:05:07 
----------------------------------------------------------------------------
9PXD257              | Mesa License Plate             | 2025-04-26 22:05:52 
----------------------------------------------------------------------------
9RLN223              | Mesa License Plate             | 2025-04-26 22:01:25 
PASS: LPR Events (Non-LPOI)

--------------------------------------------------------------------------------
Running Test: LPR Events (Hourly Report)
Script: test_lpr_hourly_report_api.py
--------------------------------------------------------------------------------
  -> Using default history_hours=1
--------------------------------------------------------------------------------
Running: python -m src_helix.test_lpr_hourly_report_api --log_level INFO --history_hours 1
--------------------------------------------------------------------------------
2025-04-26 22:15:02,192 - __main__ - INFO - Successfully retrieved API token: v2_bc361c6...
2025-04-26 22:15:02,192 - __main__ - INFO - Fetching License Plates of Interest...
2025-04-26 22:15:02,192 - src_helix.api_utils - INFO - Fetching all License Plates of Interest (LPOI)...
2025-04-26 22:15:04,228 - src_helix.api_utils - INFO - Finished fetching all data from /cameras/v1/analytics/lpr/license_plate_of_interest. Total items fetched: 612
2025-04-26 22:15:04,229 - __main__ - INFO - Successfully retrieved 611 License Plates of Interest.
2025-04-26 22:15:04,229 - __main__ - INFO - Fetching LPR-enabled cameras...
2025-04-26 22:15:04,229 - src_helix.api_utils - INFO - Fetching all cameras...
2025-04-26 22:15:05,007 - src_helix.api_utils - INFO - Finished fetching all data from /cameras/v1/devices. Total items fetched: 10
2025-04-26 22:15:05,007 - src_helix.api_utils - INFO - Found 5 LPR-enabled cameras (filtered by 'License' in name).
2025-04-26 22:15:05,007 - __main__ - INFO - Querying ALL LPR images for the last 1 hours...
2025-04-26 22:15:05,007 - __main__ - INFO - Time range: 2025-04-26 21:15:05 to 2025-04-26 22:15:05
2025-04-26 22:15:05,007 - __main__ - INFO - Fetching LPR images for camera: Mesa License Plate (ID: 2bc18656-7a1e-4612-b08a-4e1ae47364f0)
2025-04-26 22:15:08,716 - src_helix.api_utils - INFO - Finished fetching LPR images for camera 2bc18656-7a1e-4612-b08a-4e1ae47364f0. Total detections: 19
2025-04-26 22:15:08,716 - __main__ - INFO - Fetching LPR images for camera: Highland License Plate (ID: 8c219867-9e7a-40e1-b19d-020f7458558c)
2025-04-26 22:15:11,276 - src_helix.api_utils - INFO - Finished fetching LPR images for camera 8c219867-9e7a-40e1-b19d-020f7458558c. Total detections: 0
2025-04-26 22:15:11,277 - __main__ - INFO - Fetching LPR images for camera: Main Gate Exit License Plates (ID: ab34699a-038b-41b4-98b4-9d83055489b6)
2025-04-26 22:15:14,248 - src_helix.api_utils - INFO - Finished fetching LPR images for camera ab34699a-038b-41b4-98b4-9d83055489b6. Total detections: 0
2025-04-26 22:15:14,248 - __main__ - INFO - Fetching LPR images for camera: Mesa Exit License Plate (ID: d1e37446-ca48-4398-9243-49a99ea4bc80)
2025-04-26 22:15:17,214 - src_helix.api_utils - INFO - Finished fetching LPR images for camera d1e37446-ca48-4398-9243-49a99ea4bc80. Total detections: 8
2025-04-26 22:15:17,214 - __main__ - INFO - Fetching LPR images for camera: Main Gate License Plate  (ID: f9cd473f-3794-4bee-825c-d1ae60d8e791)
2025-04-26 22:15:23,461 - src_helix.api_utils - ERROR - Request Exception fetching data from /cameras/v1/analytics/lpr/images: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
2025-04-26 22:15:23,461 - src_helix.api_utils - ERROR - Failed to fetch LPR images for camera f9cd473f-3794-4bee-825c-d1ae60d8e791, page 2: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
2025-04-26 22:15:23,461 - src_helix.api_utils - INFO - Finished fetching LPR images for camera f9cd473f-3794-4bee-825c-d1ae60d8e791. Total detections: 2
2025-04-26 22:15:23,461 - __main__ - INFO - Finished fetching LPR images from all LPR-enabled cameras. Total detections fetched: 29.
2025-04-26 22:15:23,462 - __main__ - INFO - Categorizing and aggregating detections by hour...
2025-04-26 22:15:23,462 - __main__ - INFO - Finished aggregating detections. Found data for 2 distinct hours.
--------------------------------------------------------
LPR Hourly Report ::: 2025-04-26 to 2025-04-26
--------------------------------------------------------
Date       | Hour            | Non-LPOI   | LPOI      
--------------------------------------------------------
2025-04-26 | 09 PM - 10 PM   | 13         | 9         
2025-04-26 | 10 PM - 11 PM   | 7          | 0         
--------------------------------------------------------
PASS: LPR Events (Hourly Report)

--------------------------------------------------------------------------------
Running Test: LPOI List
Script: test_lpoi_api.py
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Running: python -m src_helix.test_lpoi_api --log_level INFO 
--------------------------------------------------------------------------------
2025-04-26 22:15:24,382 - __main__ - INFO - Successfully retrieved API token: v2_73b7448...
2025-04-26 22:15:24,383 - __main__ - INFO - Attempting to fetch ALL LPOI data...
2025-04-26 22:15:24,383 - src_helix.api_utils - INFO - Fetching all License Plates of Interest (LPOI)...
2025-04-26 22:15:26,125 - src_helix.api_utils - INFO - Finished fetching all data from /cameras/v1/analytics/lpr/license_plate_of_interest. Total items fetched: 612
2025-04-26 22:15:26,125 - __main__ - INFO - Successfully retrieved ALL License Plates of Interest. Found 612 items.

--- LPOI API Response (All Items) ---
[
    {
        "creation_time": 1743056268,
        "description": "where did it come in",
        "license_plate": "PRA2AP"
    },
    {
        "creation_time": 1743057314,
        "description": "where did it come in",
        "license_plate": "7TBD970"
    },
    {
        "creation_time": 1739328735,
        "description": "used CH code Prius",
        "license_plate": "7GCG639"
    },
    {
        "creation_time": 1739329484,
        "description": "used CH code 1-30 ",
        "license_plate": "43417F3"
    },
    {
        "creation_time": 1739329439,
        "description": "used CH code 1-27",
        "license_plate": "PUPPERY"
    },
    {
        "creation_time": 1739329361,
        "description": "used CH code 1-27",
        "license_plate": "USKJLV3"
    },
    {
        "creation_time": 1739329398,
        "description": "used CH code 1-27",
        "license_plate": "7ZVA396"
    },
    {
        "creation_time": 1732652520,
        "description": "unauthorized vehicle",
        "license_plate": "8YEN492"
    },
    {
        "creation_time": 1743047373,
        "description": "unauthorized entry",
        "license_plate": "8XIZ633"
    },
    {
        "creation_time": 1745642472,
        "description": "u turn tailgate 4/25",
        "license_plate": "KDJENT"
    },
    {
        "creation_time": 1745640075,
        "description": "u turn slow 4/26/25",
        "license_plate": "4WPX922"
    },
    {
        "creation_time": 1745640170,
        "description": "u turn slow 4/26/25",
        "license_plate": "4WPY922"
    },
    {
        "creation_time": 1745546066,
        "description": "u turn slow 4/24/25",
        "license_plate": "71516E2"
    },
    {
        "creation_time": 1745461793,
        "description": "u turn slow 4/23/25",
        "license_plate": "9JVJ724"
    },
    {
        "creation_time": 1745459519,
        "description": "u turn slow 4/23/25",
        "license_plate": "9RLJ458"
    },
    {
        "creation_time": 1744429738,
        "description": "u turn old plate",
        "license_plate": "DA0AC"
    },
    {
        "creation_time": 1744429700,
        "description": "u turn old jeep",
        "license_plate": "DAAA"
    },
    {
        "creation_time": 1745640669,
        "description": "u turn fast 4/26/25",
        "license_plate": "5WBG354"
    },
    {
        "creation_time": 1745719291,
        "description": "u turn fast 4/26/25",
        "license_plate": "5FE1407"
    },
    {
        "creation_time": 1745641966,
        "description": "u turn fast 4/25/25",
        "license_plate": "7NFG567"
    },
    {
        "creation_time": 1745642622,
        "description": "u turn fast 4/25/25",
        "license_plate": "9PPL090"
    },
    {
        "creation_time": 1745642145,
        "description": "u turn fast 4/25/25",
        "license_plate": "6E30844"
    },
    {
        "creation_time": 1745544300,
        "description": "u turn fast 4/24/25",
        "license_plate": "4CKJ867"
    },
    {
        "creation_time": 1745544463,
        "description": "u turn fast 4/24/25",
        "license_plate": "9JLA791"
    },
    {
        "creation_time": 1744429590,
        "description": "u turn Pipes Plumb",
        "license_plate": "58051M3"
    },
    {
        "creation_time": 1745637878,
        "description": "u turn @Mesa&HL 4/25",
        "license_plate": "15393E3"
    },
    {
        "creation_time": 1744261776,
        "description": "u turn 4/9/25",
        "license_plate": "T0PNTC1"
    },
    {
        "creation_time": 1744261364,
        "description": "u turn 4/9/25",
        "license_plate": "6YME499"
    },
    {
        "creation_time": 1744159680,
        "description": "u turn 4/8/25",
        "license_plate": "8LRN282"
    },
    {
        "creation_time": 1744260495,
        "description": "u turn 4/8/25",
        "license_plate": "9D0K281"
    },
    {
        "creation_time": 1744255670,
        "description": "u turn 4/8/25",
        "license_plate": "CRD5679"
    },
    {
        "creation_time": 1744261089,
        "description": "u turn 4/8/25",
        "license_plate": "9BRT184"
    },
    {
        "creation_time": 1745297202,
        "description": "u turn 4/21/25",
        "license_plate": "CHP3875"
    },
    {
        "creation_time": 1745199680,
        "description": "u turn 4/20/25",
        "license_plate": "9ESB929"
    },
    {
        "creation_time": 1745205938,
        "description": "u turn 4/20/25",
        "license_plate": "7HRJ395"
    },
    {
        "creation_time": 1745008777,
        "description": "u turn 4/18/25",
        "license_plate": "00733H3"
    },
    {
        "creation_time": 1745026011,
        "description": "u turn 4/18/25",
        "license_plate": "8RNZ499"
    },
    {
        "creation_time": 1745035149,
        "description": "u turn 4/18/25",
        "license_plate": "9PDJ768"
    },
    {
        "creation_time": 1745033953,
        "description": "u turn 4/18/25",
        "license_plate": "CS21F87"
    },
    {
        "creation_time": 1745008881,
        "description": "u turn 4/18/25",
        "license_plate": "8C29901"
    },
    {
        "creation_time": 1745023780,
        "description": "u turn 4/18/25",
        "license_plate": "EA63E56"
    },
    {
        "creation_time": 1744753343,
        "description": "u turn 4/15/25",
        "license_plate": "8XPN592"
    },
    {
        "creation_time": 1744518380,
        "description": "u turn 4/12/25",
        "license_plate": "9JDH172"
    },
    {
        "creation_time": 1744430415,
        "description": "u turn 4/11/25",
        "license_plate": "09992P3"
    },
    {
        "creation_time": 1744434829,
        "description": "u turn 4/11/25",
        "license_plate": "9FJC550"
    },
    {
        "creation_time": 1744426896,
        "description": "u turn 4/11/25",
        "license_plate": "6PLX360"
    },
    {
        "creation_time": 1744336310,
        "description": "u turn 4/10/25",
        "license_plate": "8UUG443"
    },
    {
        "creation_time": 1744336130,
        "description": "u turn 4/10/25",
        "license_plate": "9BDX858"
    },
    {
        "creation_time": 1744336390,
        "description": "u turn 4/10/25",
        "license_plate": "8VAB238"
    },
    {
        "creation_time": 1744076170,
        "description": "u turn",
        "license_plate": "9JWK149"
    },
    {
        "creation_time": 1743043114,
        "description": "turned around & left",
        "license_plate": "8YPB382"
    },
    {
        "creation_time": 1743043079,
        "description": "turned around & left",
        "license_plate": "65011P3"
    },
    {
        "creation_time": 1743053536,
        "description": "turned & left 2X",
        "license_plate": "XTERMITE"
    },
    {
        "creation_time": 1743055153,
        "description": "turned & left",
        "license_plate": "9BQU119"
    },
    {
        "creation_time": 1743055055,
        "description": "turned & left",
        "license_plate": "5ZRS694"
    },
    {
        "creation_time": 1728766777,
        "description": "trespassing???",
        "license_plate": "8T0W756"
    },
    {
        "creation_time": 1745554333,
        "description": "tenant jaxon Knievel",
        "license_plate": "DENSDL0N"
    },
    {
        "creation_time": 1745554269,
        "description": "tenant Jaxon Knievel",
        "license_plate": "AE924V"
    },
    {
        "creation_time": 1734135856,
        "description": "tailgate red truck",
        "license_plate": "0M30501"
    },
    {
        "creation_time": 1741766339,
        "description": "tailgate on Mar 11",
        "license_plate": "01121B2"
    },
    {
        "creation_time": 1744086643,
        "description": "tailgate deliv (Hunt",
        "license_plate": "9FYY560"
    },
    {
        "creation_time": 1737186177,
        "description": "tailgate blak Tesla ",
        "license_plate": "8TAB867"
    },
    {
        "creation_time": 1739329754,
        "description": "tailgate VW Taos",
        "license_plate": "9CSV434"
    },
    {
        "creation_time": 1738658875,
        "description": "tailgate Toyota Yari",
        "license_plate": "6RLR549"
    },
    {
        "creation_time": 1739411787,
        "description": "tailgate Mercede bla",
        "license_plate": "9AKE437"
    },
    {
        "creation_time": 1734581841,
        "description": "tailgate F aft Wayne",
        "license_plate": "6WEN571"
    },
    {
        "creation_time": 1739413530,
        "description": "tailgate Bk Mercedes",
        "license_plate": "6YDC814"
    },
    {
        "creation_time": 1738467844,
        "description": "tailgate @1-31 3:34p",
        "license_plate": "8EJA865"
    },
    {
        "creation_time": 1736488741,
        "description": "tailgate 1/9/25 2pm ",
        "license_plate": "4YDN381"
    },
    {
        "creation_time": 1744431461,
        "description": "tailg Sateesh Arjula",
        "license_plate": "86453F2"
    },
    {
        "creation_time": 1743054385,
        "description": "suspicious how got i",
        "license_plate": "K982H1"
    },
    {
        "creation_time": 1731045335,
        "description": "suspicious Rob fire",
        "license_plate": "H8ASH"
    },
    {
        "creation_time": 1734592485,
        "description": "rug van tailgate",
        "license_plate": "12658F2"
    },
    {
        "creation_time": 1742838096,
        "description": "repeat offender",
        "license_plate": "29020H2"
    },
    {
        "creation_time": 1734141531,
        "description": "reg tag of OC police",
        "license_plate": "7KUX814"
    },
    {
        "creation_time": 1743986463,
        "description": "ran gate, exit 1 min",
        "license_plate": "9LUX778"
    },
    {
        "creation_time": 1740292089,
        "description": "ran exit gate feb 22",
        "license_plate": "8WXJ746"
    },
    {
        "creation_time": 1740006883,
        "description": "ran exit gate Corkys",
        "license_plate": "59736Y2"
    },
    {
        "creation_time": 1741373352,
        "description": "qtr trash can clean",
        "license_plate": "13585L3"
    },
    {
        "creation_time": 1733976015,
        "description": "pool matt Ben Errez",
        "license_plate": "46889K2"
    },
    {
        "creation_time": 1730275917,
        "description": "pool Tristan Karla",
        "license_plate": "06817P3"
    },
    {
        "creation_time": 1738559170,
        "description": "pickup tailgate 1-26",
        "license_plate": "25315U1"
    },
    {
        "creation_time": 1731992542,
        "description": "illegit? how got in?",
        "license_plate": "8NJC358"
    },
    {
        "creation_time": 1743983490,
        "description": "fake amazon violator",
        "license_plate": "7AEJ570"
    },
    {
        "creation_time": 1742448267,
        "description": "exit gate in Mesa",
        "license_plate": "9RSV459"
    },
    {
        "creation_time": 1745297573,
        "description": "drop gregson @Mesa",
        "license_plate": "FL07936"
    },
    {
        "creation_time": 1743052524,
        "description": "drive-by 3X 3/4&3/25",
        "license_plate": "FLYBAHA"
    },
    {
        "creation_time": 1745639905,
        "description": "code! Octa Scutelnic",
        "license_plate": "CLASY22"
    },
    {
        "creation_time": 1732572059,
        "description": "cleaning Hal Bassett",
        "license_plate": "9JBM295"
    },
    {
        "creation_time": 1731430833,
        "description": "cleanin Sarah Graves",
        "license_plate": "81666R1"
    },
    {
        "creation_time": 1733343798,
        "description": "cabinet Mike Lively",
        "license_plate": "8TMR679"
    },
    {
        "creation_time": 1738536710,
        "description": "attempt illegal entr",
        "license_plate": "8ZFS985"
    },
    {
        "creation_time": 1743053783,
        "description": "another xtermite!!!",
        "license_plate": "7FDC817"
    },
    {
        "creation_time": 1744524514,
        "description": "X ram exit gate 4/12",
        "license_plate": "9PHS546"
    },
    {
        "creation_time": 1744523216,
        "description": "X ram exit estate sa",
        "license_plate": "9KTC004"
    },
    {
        "creation_time": 1744520641,
        "description": "X Kelly Ramirez X",
        "license_plate": "91929B4"
    },
    {
        "creation_time": 1744088603,
        "description": "Why D Fernandez open",
        "license_plate": "8SHG011"
    },
    {
        "creation_time": 1737957626,
        "description": "White Audi trespass",
        "license_plate": "8ZUG194"
    },
    {
        "creation_time": 1729376801,
        "description": "Vic Bartolo Korinek",
        "license_plate": "55367F3"
    },
    {
        "creation_time": 1744262810,
        "description": "Vet donate Milliken\u221a",
        "license_plate": "02813K2"
    },
    {
        "creation_time": 1728854564,
        "description": "Venancia V Lostetter",
        "license_plate": "7AGM063"
    },
    {
        "creation_time": 1745554755,
        "description": "VanBerg  Jim Fornaca",
        "license_plate": "68170H3"
    },
    {
        "creation_time": 1743133778,
        "description": "VCWD",
        "license_plate": "1590809"
    },
    {
        "creation_time": 1745024138,
        "description": "V door&gate Engel \u221a",
        "license_plate": "45479C2"
    },
    {
        "creation_time": 1744336350,
        "description": "V cleaning Ozkan",
        "license_plate": "8SSF503"
    },
    {
        "creation_time": 1745023968,
        "description": "V clean Rosa Gonzale",
        "license_plate": "9DCZ697"
    },
    {
        "creation_time": 1745024031,
        "description": "V clean Izzy Hermosi",
        "license_plate": "6JVY321"
    },
    {
        "creation_time": 1745026192,
        "description": "V clean Ben Errez \u221a",
        "license_plate": "7BJT986"
    },
    {
        "creation_time": 1744261215,
        "description": "V Zipse Hermosillo \u221a",
        "license_plate": "88087A4"
    },
    {
        "creation_time": 1745297809,
        "description": "V Zain Ellen Molla \u221a",
        "license_plate": "9MRY671"
    },
    {
        "creation_time": 1744430243,
        "description": "V Tim Milliken \u221a",
        "license_plate": "44284Y2"
    },
    {
        "creation_time": 1745197307,
        "description": "V Thomas Chung \u221a",
        "license_plate": "DD76B65"
    },
    {
        "creation_time": 1744335688,
        "description": "V Terrence Martin \u221a",
        "license_plate": "7VEL637"
    },
    {
        "creation_time": 1744434417,
        "description": "V Stu Oster \u221a",
        "license_plate": "63093B2"
    },
    {
        "creation_time": 1745388000,
        "description": "V Stu Oster \u221a",
        "license_plate": "8SQR615"
    },
    {
        "creation_time": 1744427279,
        "description": "V Stu Oster \u221a",
        "license_plate": "19846M3"
    },
    {
        "creation_time": 1745544551,
        "description": "V Stu Oster \u221a",
        "license_plate": "04470W3"
    },
    {
        "creation_time": 1744336700,
        "description": "V Stu Oster \u221a",
        "license_plate": "9JIN933"
    },
    {
        "creation_time": 1745544816,
        "description": "V Scott Furgerson \u221a",
        "license_plate": "45259F3"
    },
    {
        "creation_time": 1745387332,
        "description": "V Sateesh Arjula \u221a",
        "license_plate": "4TX3500"
    },
    {
        "creation_time": 1743902759,
        "description": "V Sarah Graves \u221a",
        "license_plate": "8H31407"
    },
    {
        "creation_time": 1745459206,
        "description": "V Ryder Paxton \u221a",
        "license_plate": "8LIW249"
    },
    {
        "creation_time": 1745033233,
        "description": "V Ryder Paxton \u221a",
        "license_plate": "8TNP045"
    },
    {
        "creation_time": 1745641453,
        "description": "V Rosa Gonzalez \u221a",
        "license_plate": "9MER699"
    },
    {
        "creation_time": 1744262516,
        "description": "V Rosa Byung Kang \u221a",
        "license_plate": "7MPB399"
    },
    {
        "creation_time": 1743055223,
        "description": "V Romero Paint Livel",
        "license_plate": "17311F2"
    },
    {
        "creation_time": 1744514799,
        "description": "V Roberto Lozano \u221a",
        "license_plate": "79143J3"
    },
    {
        "creation_time": 1743040407,
        "description": "V Roberto Lozano \u221a",
        "license_plate": "8CXY011"
    },
    {
        "creation_time": 1744522654,
        "description": "V Robert Tahiry \u221a",
        "license_plate": "8HKE304"
    },
    {
        "creation_time": 1745719920,
        "description": "V Robert Tahiry \u221a",
        "license_plate": "7TNC370"
    },
    {
        "creation_time": 1745023910,
        "description": "V Rivera garde Molla",
        "license_plate": "52825X2"
    },
    {
        "creation_time": 1745025273,
        "description": "V Rick Engel \u221a",
        "license_plate": "38856L3"
    },
    {
        "creation_time": 1745025969,
        "description": "V Rick Engel \u221a",
        "license_plate": "PLGINVN"
    },
    {
        "creation_time": 1744518279,
        "description": "V Richard Mallo \u221a",
        "license_plate": "8JCE167"
    },
    {
        "creation_time": 1745197079,
        "description": "V Richard Mallo \u221a",
        "license_plate": "MARKRYM"
    },
    {
        "creation_time": 1745035420,
        "description": "V Raquelita Lugo \u221a",
        "license_plate": "9PUV859"
    },
    {
        "creation_time": 1743987328,
        "description": "V Raquelita Lugo \u221a",
        "license_plate": "EA59Y71"
    },
    {
        "creation_time": 1744337203,
        "description": "V Raquelita Lugo \u221a",
        "license_plate": "5VPD780"
    },
    {
        "creation_time": 1730059116,
        "description": "V Power Pet Levy",
        "license_plate": "FWA5205"
    },
    {
        "creation_time": 1741853811,
        "description": "V Pool Kim DeBow \u221a",
        "license_plate": "57710D3"
    },
    {
        "creation_time": 1741854536,
        "description": "V Pool Hal Bassett",
        "license_plate": "54604D4"
    },
    {
        "creation_time": 1744430583,
        "description": "V Paula Furgerson \u221a",
        "license_plate": "8BZC483"
    },
    {
        "creation_time": 1744426540,
        "description": "V Paula Furgerson \u221a",
        "license_plate": "8FDS640"
    },
    {
        "creation_time": 1744427010,
        "description": "V Paula Furgerson \u221a",
        "license_plate": "8LDV893"
    },
    {
        "creation_time": 1743985241,
        "description": "V Paula Furgerson \u221a",
        "license_plate": "9LCP130"
    },
    {
        "creation_time": 1744427173,
        "description": "V Paula Furgerson \u221a",
        "license_plate": "8UAU299"
    },
    {
        "creation_time": 1744424936,
        "description": "V Paula Furgerson \u221a",
        "license_plate": "9JXY141"
    },
    {
        "creation_time": 1744426646,
        "description": "V Paula Furgerson \u221a",
        "license_plate": "5VVZ527"
    },
    {
        "creation_time": 1744426829,
        "description": "V Paula Furgerson \u221a",
        "license_plate": "9HSK635"
    },
    {
        "creation_time": 1744427080,
        "description": "V Paula Furgerson \u221a",
        "license_plate": "65312U3"
    },
    {
        "creation_time": 1744425471,
        "description": "V Paula Furgerson \u221a",
        "license_plate": "6M71408"
    },
    {
        "creation_time": 1744426411,
        "description": "V Paula Furgerson ? ",
        "license_plate": "9ESK877"
    },
    {
        "creation_time": 1744425808,
        "description": "V Paula Fergerson \u221a",
        "license_plate": "8RWW237"
    },
    {
        "creation_time": 1743899722,
        "description": "V Paola Noel \u221a ?",
        "license_plate": "8GFU539"
    },
    {
        "creation_time": 1744261424,
        "description": "V Orkin Lugo \u221a",
        "license_plate": "74722H3"
    },
    {
        "creation_time": 1743055965,
        "description": "V Octav Scutelnicu \u221a",
        "license_plate": "90825M1"
    },
    {
        "creation_time": 1743048665,
        "description": "V Noveline Mallo \u221a",
        "license_plate": "72316R3"
    },
    {
        "creation_time": 1745642089,
        "description": "V Noveline Mallo \u221a",
        "license_plate": "8UUR656"
    },
    {
        "creation_time": 1745641624,
        "description": "V Noveline Mallo \u221a",
        "license_plate": "7XRE742"
    },
    {
        "creation_time": 1744426735,
        "description": "V Noveline Mallo \u221a",
        "license_plate": "17037J2"
    },
    {
        "creation_time": 1743681769,
        "description": "V Natasha Sawh \u221a",
        "license_plate": "444073D"
    },
    {
        "creation_time": 1743133959,
        "description": "V MyGuy HVAC",
        "license_plate": "35819S2"
    },
    {
        "creation_time": 1743899546,
        "description": "V Morgen Perez \u221a",
        "license_plate": "9JTT951"
    },
    {
        "creation_time": 1743900915,
        "description": "V Morgan Perez \u221a",
        "license_plate": "8ZVT345"
    },
    {
        "creation_time": 1743054562,
        "description": "V Mohammad Molla \u221a",
        "license_plate": "8N0H036"
    },
    {
        "creation_time": 1743055713,
        "description": "V Mohammad Molla \u221a",
        "license_plate": "9CGX330"
    },
    {
        "creation_time": 1743055865,
        "description": "V Mohammad Molla \u221a",
        "license_plate": "9GFS537"
    },
    {
        "creation_time": 1743987450,
        "description": "V Mike Sobh \u221a",
        "license_plate": "79645C3"
    },
    {
        "creation_time": 1743907212,
        "description": "V Mike Salm Lively \u221a",
        "license_plate": "90815E3"
    },
    {
        "creation_time": 1744155228,
        "description": "V Melanie Thompson \u221a",
        "license_plate": "9MTH081"
    },
    {
        "creation_time": 1745642263,
        "description": "V Melanie Thompson \u221a",
        "license_plate": "8WFN814"
    },
    {
        "creation_time": 1744334890,
        "description": "V Melanie Thompson \u221a",
        "license_plate": "62239N2"
    },
    {
        "creation_time": 1744160116,
        "description": "V Melanie Thompson \u221a",
        "license_plate": "9RFF217"
    },
    {
        "creation_time": 1743987031,
        "description": "V Mehmet Firat \u221a",
        "license_plate": "8KES497"
    },
    {
        "creation_time": 1744519926,
        "description": "V Mehmet Fira Ozkan\u221a",
        "license_plate": "8EUL294"
    },
    {
        "creation_time": 1743047090,
        "description": "V Mauzy HVAC Errez \u221a",
        "license_plate": "22693T3"
    },
    {
        "creation_time": 1730146551,
        "description": "V Martiniz Jame Shin",
        "license_plate": "82385K1"
    },
    {
        "creation_time": 1743046817,
        "description": "V Martin Wronski \u221a",
        "license_plate": "95395F1"
    },
    {
        "creation_time": 1744433686,
        "description": "V Martin Wronski \u221a",
        "license_plate": "9KTD548"
    },
    {
        "creation_time": 1744172084,
        "description": "V Mark Ramos \u221a",
        "license_plate": "CKT4200"
    },
    {
        "creation_time": 1745545153,
        "description": "V Mark Ramos \u221a",
        "license_plate": "DVF9866"
    },
    {
        "creation_time": 1743040558,
        "description": "V Mark Ramos \u221a",
        "license_plate": "8RRA992"
    },
    {
        "creation_time": 1744265556,
        "description": "V Mark Ramos \u221a",
        "license_plate": "6SKH282"
    },
    {
        "creation_time": 1745546214,
        "description": "V Marc Wrona \u221a",
        "license_plate": "9BPX919"
    },
    {
        "creation_time": 1745719987,
        "description": "V Madina Tahiry \u221a",
        "license_plate": "9HYB970"
    },
    {
        "creation_time": 1743984852,
        "description": "V Lupita4care Kang \u221a",
        "license_plate": "8L0B745"
    },
    {
        "creation_time": 1728854389,
        "description": "V Lupita Anne Kang",
        "license_plate": "8HNB204"
    },
    {
        "creation_time": 1744262921,
        "description": "V Luis Paint Perez \u221a",
        "license_plate": "56579Y1"
    },
    {
        "creation_time": 1743986346,
        "description": "V Logan Scully \u221a",
        "license_plate": "9PGX936"
    },
    {
        "creation_time": 1744171737,
        "description": "V Lloyd Pest Lugo \u221a",
        "license_plate": "59426J3"
    },
    {
        "creation_time": 1743986037,
        "description": "V Lina Molla \u221a",
        "license_plate": "8KLL837"
    },
    {
        "creation_time": 1744434092,
        "description": "V Lina Molla \u221a",
        "license_plate": "01024E4"
    },
    {
        "creation_time": 1744160470,
        "description": "V Lifetime A Perez \u221a",
        "license_plate": "2Z54729"
    },
    {
        "creation_time": 1743054141,
        "description": "V Kelly Scutelnicu \u221a",
        "license_plate": "9GEN780"
    },
    {
        "creation_time": 1744430372,
        "description": "V Kelley Scutelnicu\u221a",
        "license_plate": "8ZMV910"
    },
    {
        "creation_time": 1745032596,
        "description": "V Kathy Ochoa Anand",
        "license_plate": "8HMA960"
    },
    {
        "creation_time": 1745196651,
        "description": "V Kathlee Delmastro\u221a",
        "license_plate": "7SKS486"
    },
    {
        "creation_time": 1745199033,
        "description": "V Kathle Delmastro \u221a",
        "license_plate": "8YKG726"
    },
    {
        "creation_time": 1745199787,
        "description": "V Kathle Delmastro \u221a",
        "license_plate": "8XHH857"
    },
    {
        "creation_time": 1745199612,
        "description": "V Kathle Delmastro \u221a",
        "license_plate": "BACMAGC"
    },
    {
        "creation_time": 1745719487,
        "description": "V Kathle Delmastro \u221a",
        "license_plate": "9MED309"
    },
    {
        "creation_time": 1745386167,
        "description": "V Karla Hernandaz \u221a",
        "license_plate": "02124R3"
    },
    {
        "creation_time": 1745387534,
        "description": "V Juliet Navas \u221a",
        "license_plate": "PPA537"
    },
    {
        "creation_time": 1745025839,
        "description": "V Jon Fagerstrom \u221a",
        "license_plate": "8NXL629"
    },
    {
        "creation_time": 1745198889,
        "description": "V John Delmastro \u221a",
        "license_plate": "8MQG664"
    },
    {
        "creation_time": 1745025040,
        "description": "V JessLopez Thompson",
        "license_plate": "35192S1"
    },
    {
        "creation_time": 1743055435,
        "description": "V Jennie Concannon \u221a",
        "license_plate": "90698M2"
    },
    {
        "creation_time": 1744173040,
        "description": "V Jennie Concannon \u221a",
        "license_plate": "8YHU910"
    },
    {
        "creation_time": 1745025165,
        "description": "V Jennie Concannon \u221a",
        "license_plate": "07538E2"
    },
    {
        "creation_time": 1744522340,
        "description": "V Jennie Concannon \u221a",
        "license_plate": "9GTC632"
    },
    {
        "creation_time": 1744161524,
        "description": "V Jeff Johnston \u221a",
        "license_plate": "10465X2"
    },
    {
        "creation_time": 1744170725,
        "description": "V Jeff Johnston \u221a",
        "license_plate": "71822C3"
    },
    {
        "creation_time": 1745643653,
        "description": "V Jaime Ramirez \u221a",
        "license_plate": "5FGP840"
    },
    {
        "creation_time": 1743047003,
        "description": "V Jaime Ramirez \u221a",
        "license_plate": "4WJ4023"
    },
    {
        "creation_time": 1742176923,
        "description": "V Izzy Hermosillo \u221a",
        "license_plate": "8EJW729"
    },
    {
        "creation_time": 1743047577,
        "description": "V Isaiah Ramos \u221a",
        "license_plate": "9F0V307"
    },
    {
        "creation_time": 1743133545,
        "description": "V Hydrex Pest Contro",
        "license_plate": "25556F2"
    },
    {
        "creation_time": 1743048436,
        "description": "V Hussam Elfarra \u221a",
        "license_plate": "8ZVZ148"
    },
    {
        "creation_time": 1743041894,
        "description": "V Helen Wallace \u221a",
        "license_plate": "DM10DC"
    },
    {
        "creation_time": 1743050897,
        "description": "V Hana Molla \u221a",
        "license_plate": "9PTF916"
    },
    {
        "creation_time": 1743050344,
        "description": "V Hana Molla \u221a",
        "license_plate": "9MSL567"
    },
    {
        "creation_time": 1743056489,
        "description": "V HOA Landscaper",
        "license_plate": "16563J3"
    },
    {
        "creation_time": 1744433399,
        "description": "V Gregson \u221a",
        "license_plate": "6NVH546"
    },
    {
        "creation_time": 1745196410,
        "description": "V Gregson \u221a",
        "license_plate": "7EAGLE9"
    },
    {
        "creation_time": 1743906651,
        "description": "V Gregson \u221a",
        "license_plate": "7TSP639"
    },
    {
        "creation_time": 1744430052,
        "description": "V Geek Scutelnicu \u221a",
        "license_plate": "18661N2"
    },
    {
        "creation_time": 1744429976,
        "description": "V Geek Scutelnicu \u221a",
        "license_plate": "90745L3"
    },
    {
        "creation_time": 1745007594,
        "description": "V Forrest Reardon \u221a",
        "license_plate": "8TKT304"
    },
    {
        "creation_time": 1743043336,
        "description": "V Forrest Reardon \u221a",
        "license_plate": "4JSW615"
    },
    {
        "creation_time": 1743046186,
        "description": "V Forrest Reardon \u221a",
        "license_plate": "73695A4"
    },
    {
        "creation_time": 1745462275,
        "description": "V Forrest Reardon \u221a",
        "license_plate": "27797F2"
    },
    {
        "creation_time": 1743043239,
        "description": "V Fernando Lugo \u221a",
        "license_plate": "DZ73K37"
    },
    {
        "creation_time": 1743051797,
        "description": "V Fernando Lugo \u221a",
        "license_plate": "9NUR174"
    },
    {
        "creation_time": 1744155420,
        "description": "V Fernando Lugo \u221a",
        "license_plate": "12199C1"
    },
    {
        "creation_time": 1743984642,
        "description": "V Fernando Lugo \u221a",
        "license_plate": "CX83B89"
    },
    {
        "creation_time": 1745024216,
        "description": "V Erin Garcia \u221a",
        "license_plate": "9RUC488"
    },
    {
        "creation_time": 1745197431,
        "description": "V Erin Garcia \u221a",
        "license_plate": "4TEU759"
    },
    {
        "creation_time": 1745544420,
        "description": "V Erin Garcia \u221a",
        "license_plate": "9SWH053"
    },
    {
        "creation_time": 1745032802,
        "description": "V Eden Bergstrom \u221a",
        "license_plate": "GXF1021"
    },
    {
        "creation_time": 1745034971,
        "description": "V Ed Ochoa Anand",
        "license_plate": "9JXA412"
    },
    {
        "creation_time": 1744262390,
        "description": "V Dorene Shadid \u221a",
        "license_plate": "8S89000"
    },
    {
        "creation_time": 1743134028,
        "description": "V Discount Glass",
        "license_plate": "24523T1"
    },
    {
        "creation_time": 1743677458,
        "description": "V Delores Gregson \u221a",
        "license_plate": "8ZFR073"
    },
    {
        "creation_time": 1743987235,
        "description": "V Dawn Fuller \u221a",
        "license_plate": "9RVC337"
    },
    {
        "creation_time": 1745297360,
        "description": "V Dawn Fuller \u221a",
        "license_plate": "7VCA617"
    },
    {
        "creation_time": 1745387203,
        "description": "V Dawn Fuller \u221a",
        "license_plate": "8XDN649"
    },
    {
        "creation_time": 1744516846,
        "description": "V David Murdico \u221a",
        "license_plate": "9AND848"
    },
    {
        "creation_time": 1745460171,
        "description": "V David Murdico \u221a",
        "license_plate": "9NIR718"
    },
    {
        "creation_time": 1744993711,
        "description": "V David Murdico \u221a",
        "license_plate": "9LDY994"
    },
    {
        "creation_time": 1744432678,
        "description": "V David Murdico \u221a",
        "license_plate": "LW576W0"
    },
    {
        "creation_time": 1743908486,
        "description": "V Daniela Perry \u221a",
        "license_plate": "8U0F904"
    },
    {
        "creation_time": 1745025680,
        "description": "V Cynthia Engel \u221a",
        "license_plate": "79418F3"
    },
    {
        "creation_time": 1745026141,
        "description": "V Curtis Lively \u221a",
        "license_plate": "9ELK372"
    },
    {
        "creation_time": 1744265866,
        "description": "V Curtis Lively \u221a",
        "license_plate": "9MVL587"
    },
    {
        "creation_time": 1745462773,
        "description": "V Curtis Lively \u221a",
        "license_plate": "19090C4"
    },
    {
        "creation_time": 1745387913,
        "description": "V Crist Siaweleski \u221a",
        "license_plate": "CWR6128"
    },
    {
        "creation_time": 1744521657,
        "description": "V Crist Siaweleski \u221a",
        "license_plate": "ZM0M"
    },
    {
        "creation_time": 1743132660,
        "description": "V Corkys Pest",
        "license_plate": "30203D3"
    },
    {
        "creation_time": 1745640918,
        "description": "V Concannon \u221a",
        "license_plate": "04480G3"
    },
    {
        "creation_time": 1745642566,
        "description": "V Concannon \u221a",
        "license_plate": "7E96224"
    },
    {
        "creation_time": 1744429637,
        "description": "V Concannon \u221a",
        "license_plate": "DADACJ7"
    },
    {
        "creation_time": 1744264333,
        "description": "V Colleen Lister \u221a",
        "license_plate": "6N86882"
    },
    {
        "creation_time": 1744337058,
        "description": "V CCC Pool",
        "license_plate": "8D34858"
    },
    {
        "creation_time": 1743053920,
        "description": "V Byung Kang \u221a",
        "license_plate": "95995E3"
    },
    {
        "creation_time": 1744335108,
        "description": "V Byung Kang \u221a",
        "license_plate": "CX75B37"
    },
    {
        "creation_time": 1744523023,
        "description": "V Ben Errez GF \u221a",
        "license_plate": "9R0D399"
    },
    {
        "creation_time": 1745719799,
        "description": "V Batoul Tahiry \u221a",
        "license_plate": "9BDP897"
    },
    {
        "creation_time": 1743903050,
        "description": "V Barbara Victor \u221a",
        "license_plate": "8NSU673"
    },
    {
        "creation_time": 1743046279,
        "description": "V Aurora Ramirez \u221a",
        "license_plate": "49501B3"
    },
    {
        "creation_time": 1731442003,
        "description": "V Augustine Lively",
        "license_plate": "8F40244"
    },
    {
        "creation_time": 1745641907,
        "description": "V Arleen Lively \u221a",
        "license_plate": "9LZB937"
    },
    {
        "creation_time": 1744427555,
        "description": "V Ariel Bergstrom \u221a",
        "license_plate": "9APX363"
    },
    {
        "creation_time": 1744254172,
        "description": "V Ariel Bergstrom \u221a",
        "license_plate": "7NJA129"
    },
    {
        "creation_time": 1745462883,
        "description": "V Antonio Ram Lively",
        "license_plate": "85676K3"
    },
    {
        "creation_time": 1745639645,
        "description": "V Antonia Toupet \u221a",
        "license_plate": "6RRM137"
    },
    {
        "creation_time": 1744266059,
        "description": "V Anthon Siawelensi\u221a",
        "license_plate": "87527G1"
    },
    {
        "creation_time": 1743873108,
        "description": "V Ansheng Wang \u221a",
        "license_plate": "EMA6ZX"
    },
    {
        "creation_time": 1744520039,
        "description": "V Andy Etemadi \u221a",
        "license_plate": "91183N3"
    },
    {
        "creation_time": 1743132717,
        "description": "V Anderson Plumbing",
        "license_plate": "28649B3"
    },
    {
        "creation_time": 1744264960,
        "description": "V Alma Rangel \u221a",
        "license_plate": "9GJY029"
    },
    {
        "creation_time": 1744261950,
        "description": "V All Pest Korinek \u221a",
        "license_plate": "59818T3"
    },
    {
        "creation_time": 1745460995,
        "description": "V Alive Johnston \u221a",
        "license_plate": "74025V3"
    },
    {
        "creation_time": 1745639321,
        "description": "V Alejandra Perez \u221a",
        "license_plate": "9FWE056"
    },
    {
        "creation_time": 1743899000,
        "description": "V Alejandra Perez \u221a",
        "license_plate": "7AVJ298"
    },
    {
        "creation_time": 1744480418,
        "description": "V Alejandra Perez \u221a",
        "license_plate": "08557U3"
    },
    {
        "creation_time": 1745640825,
        "description": "V Alejandra Perez \u221a",
        "license_plate": "37256N3"
    },
    {
        "creation_time": 1743046656,
        "description": "V Alejandra Perez \u221a",
        "license_plate": "9MYL548"
    },
    {
        "creation_time": 1743901858,
        "description": "V Aden Pest Perez \u221a",
        "license_plate": "9CLT547"
    },
    {
        "creation_time": 1744517620,
        "description": "V Adam Levy \u221a 4/11?",
        "license_plate": "8ETJ394"
    },
    {
        "creation_time": 1743986100,
        "description": "V Adam Levy \u221a",
        "license_plate": "9CGL972"
    },
    {
        "creation_time": 1744172669,
        "description": "V Acces door Engel \u221a",
        "license_plate": "09786A3"
    },
    {
        "creation_time": 1745025529,
        "description": "V Abby Ramos \u221a",
        "license_plate": "9HHS956"
    },
    {
        "creation_time": 1743987681,
        "description": "V AKYM trailer \u221a",
        "license_plate": "4WA4160"
    },
    {
        "creation_time": 1743043034,
        "description": "V AKYM Property \u221a",
        "license_plate": "12452K2"
    },
    {
        "creation_time": 1744090361,
        "description": "V AKYM Prop \u221a",
        "license_plate": "9KIV977"
    },
    {
        "creation_time": 1737251409,
        "description": "Uniuni delivery man",
        "license_plate": "9PVT475"
    },
    {
        "creation_time": 1739483675,
        "description": "Union Tribune Trinid",
        "license_plate": "8TVN509"
    },
    {
        "creation_time": 1745033892,
        "description": "Uber Adam Levy",
        "license_plate": "8CZJ962"
    },
    {
        "creation_time": 1734210830,
        "description": "UPS Jason #605676",
        "license_plate": "16759X1"
    },
    {
        "creation_time": 1745702968,
        "description": "UPS #638007",
        "license_plate": "79862L3"
    },
    {
        "creation_time": 1743873521,
        "description": "U turned & left",
        "license_plate": "N8A42L7"
    },
    {
        "creation_time": 1743983866,
        "description": "U turn 3X@Mesa",
        "license_plate": "7TGZ994"
    },
    {
        "creation_time": 1743893921,
        "description": "U turn & left",
        "license_plate": "9SCX976"
    },
    {
        "creation_time": 1743901494,
        "description": "U turn & left",
        "license_plate": "9HJS094"
    },
    {
        "creation_time": 1743896697,
        "description": "U turn & left",
        "license_plate": "7BWT116"
    },
    {
        "creation_time": 1743893805,
        "description": "U turn & left",
        "license_plate": "7VZK287"
    },
    {
        "creation_time": 1743894140,
        "description": "U turn & left",
        "license_plate": "9JTL655"
    },
    {
        "creation_time": 1743990918,
        "description": "U turn ",
        "license_plate": "BEXD453"
    },
    {
        "creation_time": 1744086257,
        "description": "U turn",
        "license_plate": "8MSX802"
    },
    {
        "creation_time": 1744248259,
        "description": "U turn",
        "license_plate": "GMH600"
    },
    {
        "creation_time": 1743984716,
        "description": "U turn",
        "license_plate": "SGC1367"
    },
    {
        "creation_time": 1743987084,
        "description": "U turn",
        "license_plate": "392TCX"
    },
    {
        "creation_time": 1743984776,
        "description": "U turn",
        "license_plate": "9MGV585"
    },
    {
        "creation_time": 1743987550,
        "description": "U turn",
        "license_plate": "8XUT002"
    },
    {
        "creation_time": 1743984436,
        "description": "U turn",
        "license_plate": "7LJG406"
    },
    {
        "creation_time": 1743984751,
        "description": "U turn",
        "license_plate": "10885R3"
    },
    {
        "creation_time": 1745546466,
        "description": "Truly pest Navas \u221a",
        "license_plate": "12725H2"
    },
    {
        "creation_time": 1731347202,
        "description": "Tino Diego Peter Kim",
        "license_plate": "6S33835"
    },
    {
        "creation_time": 1743907471,
        "description": "Thrasher Pest Morgan",
        "license_plate": "9HXF241"
    },
    {
        "creation_time": 1730148043,
        "description": "Terminix Lister",
        "license_plate": "FR61401"
    },
    {
        "creation_time": 1743910220,
        "description": "Terminix",
        "license_plate": "47603J3"
    },
    {
        "creation_time": 1745643241,
        "description": "Tenant Jaxon Knivele",
        "license_plate": "924V"
    },
    {
        "creation_time": 1745554204,
        "description": "Tenant Jaxon Knievel",
        "license_plate": "1AE924V"
    },
    {
        "creation_time": 1745643324,
        "description": "Tenant Jaxon Knievel",
        "license_plate": "E924V"
    },
    {
        "creation_time": 1731603937,
        "description": "Tailgate ",
        "license_plate": "8DUA786"
    },
    {
        "creation_time": 1745387132,
        "description": "Steve Hermosillo key",
        "license_plate": "23T8523"
    },
    {
        "creation_time": 1745642309,
        "description": "Sotero Gard Concanno",
        "license_plate": "4RW1942"
    },
    {
        "creation_time": 1730273898,
        "description": "Sotero Garcia Concan",
        "license_plate": "28460S1"
    },
    {
        "creation_time": 1744839552,
        "description": "Sheriff volunteer",
        "license_plate": "V0LUNTEER"
    },
    {
        "creation_time": 1743897181,
        "description": "Sheriff Volun23MS7S",
        "license_plate": "1594463"
    },
    {
        "creation_time": 1745301524,
        "description": "Sheriff K9 #348",
        "license_plate": "1690911"
    },
    {
        "creation_time": 1745301542,
        "description": "Sheriff #280",
        "license_plate": "1695939"
    },
    {
        "creation_time": 1730681255,
        "description": "Sergio Ga Richardson",
        "license_plate": "5R66414"
    },
    {
        "creation_time": 1730148254,
        "description": "Sebastian Lan Lister",
        "license_plate": "96036J3"
    },
    {
        "creation_time": 1730148164,
        "description": "Sebastian Lan Lister",
        "license_plate": "98853U3"
    },
    {
        "creation_time": 1729659153,
        "description": "Sean Aqua Gregson",
        "license_plate": "90990X3"
    },
    {
        "creation_time": 1732740604,
        "description": "Scott Swarin Johnson",
        "license_plate": "8P15058"
    },
    {
        "creation_time": 1730147983,
        "description": "SD Pool Lister",
        "license_plate": "35384F3"
    },
    {
        "creation_time": 1733268700,
        "description": "Ruben C Jeff Johnson",
        "license_plate": "5M89605"
    },
    {
        "creation_time": 1730761162,
        "description": "Rosario RochaSchafer",
        "license_plate": "80105F1"
    },
    {
        "creation_time": 1729533990,
        "description": "Rosa Montes D Garcia",
        "license_plate": "4ZKP643"
    },
    {
        "creation_time": 1731034802,
        "description": "Rosa Clean Wallace",
        "license_plate": "47KP643"
    },
    {
        "creation_time": 1732298041,
        "description": "Romero Paint Lively",
        "license_plate": "4W0Z350"
    },
    {
        "creation_time": 1737503643,
        "description": "Romero Esli Garcia L",
        "license_plate": "20238K3"
    },
    {
        "creation_time": 1731045171,
        "description": "Rob firefight carpen",
        "license_plate": "9DJU494"
    },
    {
        "creation_time": 1732645147,
        "description": "Remero Alonso Lively",
        "license_plate": "8WLJ551"
    },
    {
        "creation_time": 1729126445,
        "description": "Refreshing Pool Hal ",
        "license_plate": "13310G1"
    },
    {
        "creation_time": 1729630925,
        "description": "Ray Master Craft",
        "license_plate": "8HKV864"
    },
    {
        "creation_time": 1731014372,
        "description": "Randall R Pool Lugo",
        "license_plate": "66842L1"
    },
    {
        "creation_time": 1731274786,
        "description": "Ramon Drywall Lively",
        "license_plate": "48076A3"
    },
    {
        "creation_time": 1745007212,
        "description": "RainGutter Michaels\u221a",
        "license_plate": "7CSZ637"
    },
    {
        "creation_time": 1744425316,
        "description": "R Rick Engel \u221a",
        "license_plate": "8NSX148"
    },
    {
        "creation_time": 1744425011,
        "description": "R Paula Furgerson \u221a",
        "license_plate": "RIDE4SD"
    },
    {
        "creation_time": 1743040217,
        "description": "R Paula Furgerson",
        "license_plate": "8RUL764"
    },
    {
        "creation_time": 1743133013,
        "description": "R Delaney Tojino",
        "license_plate": "DP171PW"
    },
    {
        "creation_time": 1743041778,
        "description": "R Connor McManigal",
        "license_plate": "7GFP081"
    },
    {
        "creation_time": 1743040955,
        "description": "R Carolyn Quintero ",
        "license_plate": "9JBW225"
    },
    {
        "creation_time": 1743040448,
        "description": "R Anthony Siaweleski",
        "license_plate": "DL914833"
    },
    {
        "creation_time": 1730680399,
        "description": "PoolWizard Furgerson",
        "license_plate": "46760V1"
    },
    {
        "creation_time": 1731275046,
        "description": "Pool Bailey Sawh",
        "license_plate": "31376V3"
    },
    {
        "creation_time": 1732140740,
        "description": "Plateau Pest tailgat",
        "license_plate": "67016U2"
    },
    {
        "creation_time": 1744262437,
        "description": "Pia Courser",
        "license_plate": "7MPJ665"
    },
    {
        "creation_time": 1731034746,
        "description": "Phil G Pool Wallace",
        "license_plate": "31929G2"
    },
    {
        "creation_time": 1730059227,
        "description": "Pets Adam Levy",
        "license_plate": "JFP1899"
    },
    {
        "creation_time": 1729582300,
        "description": "Pedro Mark Gregson",
        "license_plate": "79077R2"
    },
    {
        "creation_time": 1728854499,
        "description": "Pedro Alvaro Gregson",
        "license_plate": "09636Z1"
    },
    {
        "creation_time": 1730275109,
        "description": "PattersonPo Franklin",
        "license_plate": "65652N3"
    },
    {
        "creation_time": 1731818935,
        "description": "Pacheco Landsc Mallo",
        "license_plate": "06059B3"
    },
    {
        "creation_time": 1731818898,
        "description": "Pacheco Landsc Mallo",
        "license_plate": "6X95481"
    },
    {
        "creation_time": 1742281115,
        "description": "Orion John Santhoff",
        "license_plate": "9CVF514"
    },
    {
        "creation_time": 1736194530,
        "description": "OnTrac van broke arm",
        "license_plate": "07134N3"
    },
    {
        "creation_time": 1743873756,
        "description": "OnTrac Gustav Sunser",
        "license_plate": "87745J3"
    },
    {
        "creation_time": 1745545255,
        "description": "On Trac???",
        "license_plate": "49234L3"
    },
    {
        "creation_time": 1731996295,
        "description": "OK rent van in@exit ",
        "license_plate": "3DQ776"
    },
    {
        "creation_time": 1734141575,
        "description": "OC police traffic",
        "license_plate": "6171949"
    },
    {
        "creation_time": 1733889217,
        "description": "Mrs Garcia Lively",
        "license_plate": "9DLR404"
    },
    {
        "creation_time": 1731127974,
        "description": "Mitch McAfee Lively",
        "license_plate": "96226K3"
    },
    {
        "creation_time": 1729198647,
        "description": "Miguel OlivierToupet",
        "license_plate": "8J54115"
    },
    {
        "creation_time": 1728854459,
        "description": "Mateo Landsc Bassett",
        "license_plate": "7R12194"
    },
    {
        "creation_time": 1731128293,
        "description": "MartinSalinas Lively",
        "license_plate": "72158G1"
    },
    {
        "creation_time": 1730059317,
        "description": "Maricela Clean Levy",
        "license_plate": "7LHD532"
    },
    {
        "creation_time": 1743908268,
        "description": "Marcus for Mike Sobh",
        "license_plate": "81141T3"
    },
    {
        "creation_time": 1743899284,
        "description": "Lyft Young Shin \u221a",
        "license_plate": "8JFD234"
    },
    {
        "creation_time": 1743872958,
        "description": "Lyft  Young Shin \u221a",
        "license_plate": "9KDT348"
    },
    {
        "creation_time": 1734368672,
        "description": "Larry@CCC Pool",
        "license_plate": "74358A4"
    },
    {
        "creation_time": 1735863152,
        "description": "Landscape DelMastro",
        "license_plate": "38248G2"
    },
    {
        "creation_time": 1741635526,
        "description": "LP open by Montemuro",
        "license_plate": "7MUH402"
    },
    {
        "creation_time": 1745545925,
        "description": "Key Sheila Khanijow",
        "license_plate": "WYN314"
    },
    {
        "creation_time": 1745641099,
        "description": "Key Phil Colonnelli",
        "license_plate": "7RQX299"
    },
    {
        "creation_time": 1743120101,
        "description": "Karla gardener",
        "license_plate": "85429K3"
    },
    {
        "creation_time": 1744841182,
        "description": "Kamps Propane Zlotni",
        "license_plate": "96048A2"
    },
    {
        "creation_time": 1736886863,
        "description": "KC Propane broke arm",
        "license_plate": "07726M1"
    },
    {
        "creation_time": 1741600359,
        "description": "Juliet Navas let in",
        "license_plate": "9PAK059"
    },
    {
        "creation_time": 1730761217,
        "description": "Juan Rocha Schafer",
        "license_plate": "8E80577"
    },
    {
        "creation_time": 1729376879,
        "description": "Josefa clean Korinek",
        "license_plate": "8LMW310"
    },
    {
        "creation_time": 1730445205,
        "description": "Jose KELLEY SCUTELNI",
        "license_plate": "88733S3"
    },
    {
        "creation_time": 1728853550,
        "description": "Jose Cruz Stu Oster",
        "license_plate": "7Z04161"
    },
    {
        "creation_time": 1730442880,
        "description": "Jose Cruz S Basinet",
        "license_plate": "46634Y1"
    },
    {
        "creation_time": 1745008814,
        "description": "John Santhoff Orion ",
        "license_plate": "8W70425"
    },
    {
        "creation_time": 1741592545,
        "description": "Jody Granger let in",
        "license_plate": "8XEJ820"
    },
    {
        "creation_time": 1732236082,
        "description": "JasonSimplePest Lowe",
        "license_plate": "48510S3"
    },
    {
        "creation_time": 1731274877,
        "description": "JabierDrywall Lively",
        "license_plate": "37854Z2"
    },
    {
        "creation_time": 1730680453,
        "description": "JC Landsc Fergerson",
        "license_plate": "16538S1"
    },
    {
        "creation_time": 1733889717,
        "description": "Izzy caretaker Kang",
        "license_plate": "6KXF366"
    },
    {
        "creation_time": 1745168625,
        "description": "Izzy Hermosillo clic",
        "license_plate": "3RLXTK"
    },
    {
        "creation_time": 1745200066,
        "description": "In by Kayla Calkins",
        "license_plate": "7PPR167"
    },
    {
        "creation_time": 1738217279,
        "description": "IT Richardo Lively",
        "license_plate": "9LEE583"
    },
    {
        "creation_time": 1728853449,
        "description": "Hughes Pool Milliken",
        "license_plate": "12020F3"
    },
    {
        "creation_time": 1745169087,
        "description": "Hssam Elfarra key",
        "license_plate": "9SHW778"
    },
    {
        "creation_time": 1744841505,
        "description": "HL exit pic\u221a no reco",
        "license_plate": "99234C4"
    },
    {
        "creation_time": 1745008708,
        "description": "HD rental Fagerstrom",
        "license_plate": "51018P3"
    },
    {
        "creation_time": 1737441991,
        "description": "Guard\u221a pool 9760LCL",
        "license_plate": "64877H3"
    },
    {
        "creation_time": 1730445044,
        "description": "Guadalupe Ibarra SCU",
        "license_plate": "94218S3"
    },
    {
        "creation_time": 1730274163,
        "description": "Griselda Concannon",
        "license_plate": "85277K3"
    },
    {
        "creation_time": 1730682222,
        "description": "Gardner Siaweleski",
        "license_plate": "21880C1"
    },
    {
        "creation_time": 1731441332,
        "description": "Gardener Tom Graves",
        "license_plate": "63957E2"
    },
    {
        "creation_time": 1731274988,
        "description": "Gardener Bailey Sawh",
        "license_plate": "37046J3"
    },
    {
        "creation_time": 1731274951,
        "description": "Gardener Bailey Sawh",
        "license_plate": "23593C2"
    },
    {
        "creation_time": 1732215079,
        "description": "Garden Morgan Perez",
        "license_plate": "40745N3"
    },
    {
        "creation_time": 1732150327,
        "description": "Gabriel gard Tanabe",
        "license_plate": "39429W3"
    },
    {
        "creation_time": 1732150292,
        "description": "Gabriel gard Tanabe",
        "license_plate": "06604P3"
    },
    {
        "creation_time": 1730059179,
        "description": "Gabriel Garden Levy",
        "license_plate": "8XGJ696"
    },
    {
        "creation_time": 1730682267,
        "description": "GL Pools Siaweleski",
        "license_plate": "17897H3"
    },
    {
        "creation_time": 1731988079,
        "description": "Frequent but no Verk",
        "license_plate": "4UMP543"
    },
    {
        "creation_time": 1743633727,
        "description": "Freight Liner Lively",
        "license_plate": "75274S3"
    },
    {
        "creation_time": 1732643877,
        "description": "Franc Marsha Michael",
        "license_plate": "87570G1"
    },
    {
        "creation_time": 1730059273,
        "description": "Fountain Andy Levy",
        "license_plate": "30139X3"
    },
    {
        "creation_time": 1745545065,
        "description": "Forrest Reardon key",
        "license_plate": "DV48146"
    },
    {
        "creation_time": 1744753085,
        "description": "Ferrellgas",
        "license_plate": "22318U1"
    },
    {
        "creation_time": 1732317564,
        "description": "Fernan handy Ramirez",
        "license_plate": "69750G2"
    },
    {
        "creation_time": 1744480631,
        "description": "Fedrico Mondragon ga",
        "license_plate": "8X91765"
    },
    {
        "creation_time": 1741631914,
        "description": "Fedex",
        "license_plate": "37383U2"
    },
    {
        "creation_time": 1743905706,
        "description": "Farmers Dog Victor\u221a",
        "license_plate": "8XQR852"
    },
    {
        "creation_time": 1744388287,
        "description": "Fallbrook Propane",
        "license_plate": "46454Y1"
    },
    {
        "creation_time": 1741637765,
        "description": "Fake Amazon,CASING?!",
        "license_plate": "9LSN414"
    },
    {
        "creation_time": 1739330354,
        "description": "F150 white broke arm",
        "license_plate": "29089H2"
    },
    {
        "creation_time": 1743906860,
        "description": "Ethan Allen Perez \u221a",
        "license_plate": "35301J3"
    },
    {
        "creation_time": 1728854122,
        "description": "Estela Alleg Martins",
        "license_plate": "8XDY060"
    },
    {
        "creation_time": 1728853979,
        "description": "Eric Rumbin Lostette",
        "license_plate": "84038H2"
    },
    {
        "creation_time": 1732317642,
        "description": "Elias Ortiz Ramirez",
        "license_plate": "8VSS845"
    },
    {
        "creation_time": 1745023682,
        "description": "Edco",
        "license_plate": "6W06472"
    },
    {
        "creation_time": 1743053264,
        "description": "EdCo pickup truck",
        "license_plate": "49247M3"
    },
    {
        "creation_time": 1743047654,
        "description": "EdCo Disposal",
        "license_plate": "8J01377"
    },
    {
        "creation_time": 1744336006,
        "description": "EdCo",
        "license_plate": "98420C4"
    },
    {
        "creation_time": 1743873639,
        "description": "DoorDash Gonzales",
        "license_plate": "8UJF777"
    },
    {
        "creation_time": 1744258475,
        "description": "Dinucci sales #9?",
        "license_plate": "8LAB513"
    },
    {
        "creation_time": 1744258390,
        "description": "Dinucci sales #8?",
        "license_plate": "8ZQU772"
    },
    {
        "creation_time": 1744258277,
        "description": "Dinucci sales #7",
        "license_plate": "6RWF398"
    },
    {
        "creation_time": 1744257938,
        "description": "Dinucci sales #6",
        "license_plate": "7YJU726"
    },
    {
        "creation_time": 1744257634,
        "description": "Dinucci sales #5",
        "license_plate": "33453T3"
    },
    {
        "creation_time": 1744257555,
        "description": "Dinucci sales #4",
        "license_plate": "8HGL592"
    },
    {
        "creation_time": 1744257412,
        "description": "Dinucci sales #3",
        "license_plate": "8ETF406"
    },
    {
        "creation_time": 1744254619,
        "description": "Dinucci sales #2",
        "license_plate": "DRS8888"
    },
    {
        "creation_time": 1744253186,
        "description": "Dinucci sales #1",
        "license_plate": "KM317"
    },
    {
        "creation_time": 1744253553,
        "description": "Dinucci sales #1",
        "license_plate": "9EKM317"
    },
    {
        "creation_time": 1730852851,
        "description": "Diana decor Gregson",
        "license_plate": "4BRN932"
    },
    {
        "creation_time": 1728853929,
        "description": "Demetrio Gar Yoke Ho",
        "license_plate": "6C82677"
    },
    {
        "creation_time": 1745170183,
        "description": "Delmastro key tesla ",
        "license_plate": "0427"
    },
    {
        "creation_time": 1744335487,
        "description": "DHL LP 23496F2",
        "license_plate": "1969"
    },
    {
        "creation_time": 1744247072,
        "description": "DHL Delivery",
        "license_plate": "88033P3"
    },
    {
        "creation_time": 1744335590,
        "description": "DHL",
        "license_plate": "23496F2"
    },
    {
        "creation_time": 1744260896,
        "description": "D? ran exit gate ",
        "license_plate": "8WFE356"
    },
    {
        "creation_time": 1745197798,
        "description": "D food  Delmastro \u221a",
        "license_plate": "06483Y3"
    },
    {
        "creation_time": 1745034483,
        "description": "D Thompson \u221a",
        "license_plate": "PMA46H"
    },
    {
        "creation_time": 1744429889,
        "description": "D Stu Oster \u221a",
        "license_plate": "96475D2"
    },
    {
        "creation_time": 1744431896,
        "description": "D Sateesh Arjula \u221a",
        "license_plate": "4NH6648"
    },
    {
        "creation_time": 1745461984,
        "description": "D Ryder Paxton \u221a",
        "license_plate": "9PBL083"
    },
    {
        "creation_time": 1744264857,
        "description": "D Rosa Gonzalez \u221a",
        "license_plate": "7SXA364"
    },
    {
        "creation_time": 1745639388,
        "description": "D Rosa Gonzalez \u221a",
        "license_plate": "8TSJ877"
    },
    {
        "creation_time": 1745641721,
        "description": "D Rosa Gonzalez \u221a",
        "license_plate": "CEM0887"
    },
    {
        "creation_time": 1745296712,
        "description": "D Rosa Gonzales \u221a",
        "license_plate": "8J0K606"
    },
    {
        "creation_time": 1745642797,
        "description": "D Mohammad Molla \u221a",
        "license_plate": "9HPA887"
    },
    {
        "creation_time": 1744264576,
        "description": "D Mohammad Molla \u221a",
        "license_plate": "9GGN023"
    },
    {
        "creation_time": 1744433837,
        "description": "D Mohammad Molla \u221a",
        "license_plate": "9JLG170"
    },
    {
        "creation_time": 1745023643,
        "description": "D Mark Ramos \u221a",
        "license_plate": "EA50W17"
    },
    {
        "creation_time": 1745459432,
        "description": "D Mark Ramos \u221a",
        "license_plate": "9HPK571"
    },
    {
        "creation_time": 1745644022,
        "description": "D Marc Wrona \u221a",
        "license_plate": "8YSC471"
    },
    {
        "creation_time": 1745719249,
        "description": "D Kelley Scutelnicu\u221a",
        "license_plate": "5VSL622"
    },
    {
        "creation_time": 1744519635,
        "description": "D Kelley Scutelnicu\u221a",
        "license_plate": "8RIM982"
    },
    {
        "creation_time": 1744519635,
        "description": "D Kelley Scutelnicu\u221a",
        "license_plate": "8RIM982"
    },
    {
        "creation_time": 1744519526,
        "description": "D Kelley Scutelnicu\u221a",
        "license_plate": "9JNL828"
    },
    {
        "creation_time": 1744338016,
        "description": "D Kelley Scutelnicu\u221a",
        "license_plate": "41850Y3"
    },
    {
        "creation_time": 1744260267,
        "description": "D Kelley Scutelnicu\u221a",
        "license_plate": "8EJP059"
    },
    {
        "creation_time": 1745386535,
        "description": "D Kathle Delmastro \u221a",
        "license_plate": "8CYB417"
    },
    {
        "creation_time": 1744434758,
        "description": "D Juliet Navas \u221a",
        "license_plate": "9KZM466"
    },
    {
        "creation_time": 1744518220,
        "description": "D John Delmastro \u221a",
        "license_plate": "9CWA348"
    },
    {
        "creation_time": 1745296852,
        "description": "D Forrest Reardon \u221a",
        "license_plate": "13382N2"
    },
    {
        "creation_time": 1745461463,
        "description": "D Fernando Lugo \u221a",
        "license_plate": "6TLX254"
    },
    {
        "creation_time": 1744480282,
        "description": "D Erin Garcia \u221a",
        "license_plate": "8YTS523"
    },
    {
        "creation_time": 1744427344,
        "description": "D Erin Garcia \u221a",
        "license_plate": "7BVM512"
    },
    {
        "creation_time": 1745171268,
        "description": "D Ariel Berstrom \u221a",
        "license_plate": "9HWU904"
    },
    {
        "creation_time": 1733451108,
        "description": "Crese cabinet Lively",
        "license_plate": "9PIU733"
    },
    {
        "creation_time": 1743903224,
        "description": "Community Glass Live",
        "license_plate": "8H56633"
    },
    {
        "creation_time": 1730275966,
        "description": "Clear pool Karla Her",
        "license_plate": "78010D2"
    },
    {
        "creation_time": 1731275015,
        "description": "Cleaning Bailey Sawh",
        "license_plate": "05307A2"
    },
    {
        "creation_time": 1732150391,
        "description": "Clara clean Tanabe",
        "license_plate": "9DGD624"
    },
    {
        "creation_time": 1739758842,
        "description": "CertaPro Pablo Marti",
        "license_plate": "07314H3"
    },
    {
        "creation_time": 1739758743,
        "description": "CertaPro Manuel Varg",
        "license_plate": "91541R2"
    },
    {
        "creation_time": 1739758783,
        "description": "CertaPro Manuel Varg",
        "license_plate": "6AAS039"
    },
    {
        "creation_time": 1739758685,
        "description": "CertaPro Dan",
        "license_plate": "8UHV554"
    },
    {
        "creation_time": 1731818970,
        "description": "Cely Ramirez Mallo",
        "license_plate": "6SIA346"
    },
    {
        "creation_time": 1744337392,
        "description": "CCC Pool use my#",
        "license_plate": "47017R2"
    },
    {
        "creation_time": 1727029793,
        "description": "CCC Pool",
        "license_plate": "5V27475"
    },
    {
        "creation_time": 1727030857,
        "description": "Burglary NV LP",
        "license_plate": "925V03"
    },
    {
        "creation_time": 1743910813,
        "description": "Bug Lots Pest",
        "license_plate": "06915V3"
    },
    {
        "creation_time": 1741854402,
        "description": "Brandon HospThompson",
        "license_plate": "6LGF223"
    },
    {
        "creation_time": 1743906727,
        "description": "Brandon Commu Glass ",
        "license_plate": "97878W3"
    },
    {
        "creation_time": 1743902043,
        "description": "Bobby Gofo Express",
        "license_plate": "5JBL222"
    },
    {
        "creation_time": 1744433555,
        "description": "B&B appliance Engel\u221a",
        "license_plate": "03003F2"
    },
    {
        "creation_time": 1731089417,
        "description": "Artemio  Vas Minkoff",
        "license_plate": "8M30501"
    },
    {
        "creation_time": 1735863697,
        "description": "Art's Marble Lively",
        "license_plate": "98584Z2"
    },
    {
        "creation_time": 1733890660,
        "description": "Art marble He Lively",
        "license_plate": "7J51023"
    },
    {
        "creation_time": 1733890715,
        "description": "Art Marble Sa Lively",
        "license_plate": "6XNK232"
    },
    {
        "creation_time": 1728853858,
        "description": "Antonio Silva Kang",
        "license_plate": "6N18348"
    },
    {
        "creation_time": 1744434558,
        "description": "Andres Reyes Landsca",
        "license_plate": "4VU5843"
    },
    {
        "creation_time": 1730274741,
        "description": "Andres Reye Franklin",
        "license_plate": "09177D3"
    },
    {
        "creation_time": 1732236014,
        "description": "Andres Landscap Lowe",
        "license_plate": "9ANW355"
    },
    {
        "creation_time": 1732235938,
        "description": "Andres Landscap Lowe",
        "license_plate": "9KUH726"
    },
    {
        "creation_time": 1730680517,
        "description": "Anastasia Furgerson",
        "license_plate": "7DED858"
    },
    {
        "creation_time": 1736886824,
        "description": "AmeriGas broke arm",
        "license_plate": "05542W3"
    },
    {
        "creation_time": 1743046901,
        "description": "Amazon?",
        "license_plate": "8KRD100"
    },
    {
        "creation_time": 1743047782,
        "description": "Amazon?",
        "license_plate": "3XMF850"
    },
    {
        "creation_time": 1743055603,
        "description": "Amazon?",
        "license_plate": "7ZVA465"
    },
    {
        "creation_time": 1743048082,
        "description": "Amazon?",
        "license_plate": "9MUU305"
    },
    {
        "creation_time": 1743054024,
        "description": "Amazon?",
        "license_plate": "9KRH993"
    },
    {
        "creation_time": 1745198431,
        "description": "Amazon+ \u221a",
        "license_plate": "9AIE294"
    },
    {
        "creation_time": 1745168382,
        "description": "Amazon \u221a no exit4/20",
        "license_plate": "9DBH339"
    },
    {
        "creation_time": 1744503984,
        "description": "Amazon \u221a no exit",
        "license_plate": "8FYP215"
    },
    {
        "creation_time": 1744424707,
        "description": "Amazon \u221a no exit",
        "license_plate": "9HFW147"
    },
    {
        "creation_time": 1744263042,
        "description": "Amazon \u221a no exit",
        "license_plate": "8GKK246"
    },
    {
        "creation_time": 1744944937,
        "description": "Amazon \u221a no exit",
        "license_plate": "8UEB803"
    },
    {
        "creation_time": 1744503870,
        "description": "Amazon \u221a no exit",
        "license_plate": "9MQR923"
    },
    {
        "creation_time": 1745294832,
        "description": "Amazon \u221a",
        "license_plate": "9RGK163"
    },
    {
        "creation_time": 1744424385,
        "description": "Amazon \u221a",
        "license_plate": "9JGJ071"
    },
    {
        "creation_time": 1745294774,
        "description": "Amazon \u221a",
        "license_plate": "8ANR180"
    },
    {
        "creation_time": 1744503798,
        "description": "Amazon \u221a",
        "license_plate": "DE30B99"
    },
    {
        "creation_time": 1744503652,
        "description": "Amazon \u221a",
        "license_plate": "8RRY385"
    },
    {
        "creation_time": 1745296443,
        "description": "Amazon \u221a",
        "license_plate": "8NEH618"
    },
    {
        "creation_time": 1745294938,
        "description": "Amazon \u221a",
        "license_plate": "9MCU994"
    },
    {
        "creation_time": 1744154990,
        "description": "Amazon \u221a",
        "license_plate": "9HDX808"
    },
    {
        "creation_time": 1744503592,
        "description": "Amazon \u221a",
        "license_plate": "9JLM838"
    },
    {
        "creation_time": 1745295249,
        "description": "Amazon \u221a",
        "license_plate": "9RAP163"
    },
    {
        "creation_time": 1744160747,
        "description": "Amazon \u221a",
        "license_plate": "8BSV661"
    },
    {
        "creation_time": 1744503732,
        "description": "Amazon \u221a",
        "license_plate": "8RUJ843"
    },
    {
        "creation_time": 1745644426,
        "description": "Amazon \u221a",
        "license_plate": "9MUB426"
    },
    {
        "creation_time": 1745296512,
        "description": "Amazon \u221a",
        "license_plate": "9E0W337"
    },
    {
        "creation_time": 1745458827,
        "description": "Amazon \u221a",
        "license_plate": "6RUF293"
    },
    {
        "creation_time": 1745294708,
        "description": "Amazon \u221a",
        "license_plate": "9KWM918"
    },
    {
        "creation_time": 1745644604,
        "description": "Amazon \u221a",
        "license_plate": "8XQR593"
    },
    {
        "creation_time": 1745294411,
        "description": "Amazon \u221a",
        "license_plate": "JN856DP"
    },
    {
        "creation_time": 1745295382,
        "description": "Amazon \u221a",
        "license_plate": "9RYK435"
    },
    {
        "creation_time": 1745034178,
        "description": "Amazon \u221a",
        "license_plate": "9NYA548"
    },
    {
        "creation_time": 1745644523,
        "description": "Amazon \u221a",
        "license_plate": "9SNS408"
    },
    {
        "creation_time": 1745458900,
        "description": "Amazon \u221a",
        "license_plate": "9CGH620"
    },
    {
        "creation_time": 1744815446,
        "description": "Amazon \u221a",
        "license_plate": "7RRG559"
    },
    {
        "creation_time": 1744424548,
        "description": "Amazon \u221a",
        "license_plate": "92633J3"
    },
    {
        "creation_time": 1744851279,
        "description": "Amazon \u221a",
        "license_plate": "9F0U741"
    },
    {
        "creation_time": 1745296303,
        "description": "Amazon \u221a",
        "license_plate": "8FSE556"
    },
    {
        "creation_time": 1744424451,
        "description": "Amazon \u221a",
        "license_plate": "7MAD835"
    },
    {
        "creation_time": 1744851692,
        "description": "Amazon \u221a",
        "license_plate": "8FJH335"
    },
    {
        "creation_time": 1745296377,
        "description": "Amazon \u221a",
        "license_plate": "9PNW482"
    },
    {
        "creation_time": 1732073590,
        "description": "Amazon regular van",
        "license_plate": "84196Y3"
    },
    {
        "creation_time": 1743910554,
        "description": "Amazon Reg van",
        "license_plate": "27997N3"
    },
    {
        "creation_time": 1745458729,
        "description": "Amazon Reg Van",
        "license_plate": "45344B4"
    },
    {
        "creation_time": 1745198601,
        "description": "Amazon Reg Van",
        "license_plate": "76217M3"
    },
    {
        "creation_time": 1741838959,
        "description": "Amazon Reg Van",
        "license_plate": "85474Y2"
    },
    {
        "creation_time": 1743900485,
        "description": "Amazon Reg Van",
        "license_plate": "60965X3"
    },
    {
        "creation_time": 1744841058,
        "description": "Amazon Reg Van",
        "license_plate": "33028Z2"
    },
    {
        "creation_time": 1732141133,
        "description": "Amazon Reg",
        "license_plate": "06237N3"
    },
    {
        "creation_time": 1745036360,
        "description": "Amazon NO key Edco",
        "license_plate": "7AFJ570"
    },
    {
        "creation_time": 1743985770,
        "description": "Amazon ?????",
        "license_plate": "9KPG701"
    },
    {
        "creation_time": 1743986230,
        "description": "Amazon ???",
        "license_plate": "8ULR085"
    },
    {
        "creation_time": 1741595419,
        "description": "Alexjandra let in ",
        "license_plate": "9D0L838"
    },
    {
        "creation_time": 1741373589,
        "description": "Alberto roof Arnie",
        "license_plate": "7V27090"
    },
    {
        "creation_time": 1728853502,
        "description": "Aida Garcia Oster",
        "license_plate": "9KXN824"
    },
    {
        "creation_time": 1744336202,
        "description": "Agent Mary Kate Lowe",
        "license_plate": "8XUJ001"
    },
    {
        "creation_time": 1743899072,
        "description": "?V Mike Sobh ?",
        "license_plate": "4M64498"
    },
    {
        "creation_time": 1743898103,
        "description": "?Trish Shin daughter",
        "license_plate": "9PXV988"
    },
    {
        "creation_time": 1743048299,
        "description": "?Hernandez Dev Serv?",
        "license_plate": "90435R3"
    },
    {
        "creation_time": 1743051049,
        "description": "??Amazon?? No exit",
        "license_plate": "9EWK926"
    },
    {
        "creation_time": 1743052037,
        "description": "???amazon??? no exit",
        "license_plate": "9RZB344"
    },
    {
        "creation_time": 1743049881,
        "description": "??? amazon? no exit",
        "license_plate": "9BEZ781"
    },
    {
        "creation_time": 1744262318,
        "description": "? amazon ? no exit",
        "license_plate": "9DEV432"
    },
    {
        "creation_time": 1744086142,
        "description": "? amazon ?",
        "license_plate": "9MYX914"
    },
    {
        "creation_time": 1744264703,
        "description": "? Amazon ? no exit",
        "license_plate": "9MDV161"
    },
    {
        "creation_time": 1744261884,
        "description": "? Amazon ? no exit",
        "license_plate": "8FCT765"
    },
    {
        "creation_time": 1744335945,
        "description": "? Amazon ?",
        "license_plate": "9FDS237"
    },
    {
        "creation_time": 1744260108,
        "description": "? Amazon ?",
        "license_plate": "9MQN606"
    },
    {
        "creation_time": 1744266191,
        "description": "? Amazon ?",
        "license_plate": "6YHL181"
    },
    {
        "creation_time": 1731730741,
        "description": "9604 MML 4",
        "license_plate": "6SDA544"
    },
    {
        "creation_time": 1731730718,
        "description": "9604 MML 3",
        "license_plate": "CZ20N01"
    },
    {
        "creation_time": 1731730688,
        "description": "9604 MML 2",
        "license_plate": "6SDN590"
    },
    {
        "creation_time": 1731730651,
        "description": "9604 MML 1",
        "license_plate": "9JTJ397"
    },
    {
        "creation_time": 1731995147,
        "description": "11/18 once old code",
        "license_plate": "8YDT204"
    },
    {
        "creation_time": 1744261691,
        "description": "+5 V Hal Bassett \u221a",
        "license_plate": "4604D4"
    },
    {
        "creation_time": 1745033337,
        "description": "! tailgate/Amazon?",
        "license_plate": "SRVFRST"
    },
    {
        "creation_time": 1744161305,
        "description": "! tailgate stay1.5hr",
        "license_plate": "5LMA721"
    },
    {
        "creation_time": 1744335298,
        "description": "! tailgate stay1.5H",
        "license_plate": "PEG785"
    },
    {
        "creation_time": 1744335840,
        "description": "! tailgate no exit",
        "license_plate": "91578H2"
    },
    {
        "creation_time": 1744338118,
        "description": "! tailgate no exit",
        "license_plate": "6FCL699"
    },
    {
        "creation_time": 1745009060,
        "description": "! tailgate Reardon",
        "license_plate": "8AKV226"
    },
    {
        "creation_time": 1744429344,
        "description": "! tailgate MT LP",
        "license_plate": "EER725"
    },
    {
        "creation_time": 1744156608,
        "description": "! tailgate Lock AKYM",
        "license_plate": "43425M2"
    },
    {
        "creation_time": 1744434942,
        "description": "! tailgate Delivery?",
        "license_plate": "DG69A55"
    },
    {
        "creation_time": 1744494249,
        "description": "! tailgate @Main",
        "license_plate": "8FJDM201"
    },
    {
        "creation_time": 1745198037,
        "description": "! tailgate 4/20//25",
        "license_plate": "9EXV927"
    },
    {
        "creation_time": 1744251557,
        "description": "! tailgate ! 4/8/25",
        "license_plate": "13648F3"
    },
    {
        "creation_time": 1744089102,
        "description": "! Ran Mesa exit gate",
        "license_plate": "VKY7110"
    },
    {
        "creation_time": 1743900394,
        "description": " ? Uniuni Villariasa",
        "license_plate": "6ZTW437"
    },
    {
        "creation_time": 1745387700,
        "description": "",
        "license_plate": "42205K3"
    },
    {
        "creation_time": 1744258730,
        "description": "",
        "license_plate": "7MYF320"
    },
    {
        "creation_time": 1744259004,
        "description": "",
        "license_plate": "7HPL354"
    }
]
2025-04-26 22:15:26,129 - src_helix.api_utils - INFO - Generated JSON template: src_helix/api-json/test_lpoi_api.json
PASS: LPOI List

--------------------------------------------------------------------------------
Running Test: Camera List
Script: test_cameras_api.py
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Running: python -m src_helix.test_cameras_api --log_level INFO 
--------------------------------------------------------------------------------
2025-04-26 22:15:27,041 - __main__ - INFO - Successfully retrieved API token: v2_dc08033...

--- Cameras API Response ---
{
    "cameras": [
        {
            "camera_id": "0fd8a0f6-1fb0-42e5-aad5-f533d46a0f32",
            "cloud_retention": 0,
            "date_added": 1637788543,
            "device_retention": 30,
            "firmware": "Up to date v2025.03.28.690925-belson-4k",
            "firmware_update_schedule": "0,86400",
            "last_online": 1745720069,
            "local_ip": "192.168.3.105",
            "location": "Verkada HQ",
            "location_angle": 0.0,
            "location_lat": 37.56564,
            "location_lon": -122.32074,
            "mac": "E0:A7:00:10:7B:E5",
            "model": "CB61-E",
            "name": "Mesa Entrance",
            "people_history_enabled": true,
            "serial": "W9PP-AQQW-JT7W",
            "site": "Mesa Gate",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "status": "Live",
            "timezone": "America/Los_Angeles",
            "vehicle_history_enabled": true
        },
        {
            "camera_id": "2bc18656-7a1e-4612-b08a-4e1ae47364f0",
            "cloud_retention": 0,
            "date_added": 1727712640,
            "device_retention": 30,
            "firmware": "Up to date v2025.04.16.695609-bruce-4k",
            "firmware_update_schedule": "0,86400",
            "last_online": 1745720095,
            "local_ip": "192.168.3.109",
            "location": "405 E 4th Ave, San Mateo, CA 94401, USA",
            "location_angle": 0.0,
            "location_lat": 33.1192068,
            "location_lon": -117.086421,
            "mac": "E0:A7:00:2B:3D:F4",
            "model": "CB62-TE",
            "name": "Mesa License Plate",
            "people_history_enabled": false,
            "serial": "TEP6-J7LE-4JEF",
            "site": "Mesa Gate",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "status": "Live",
            "timezone": "America/Los_Angeles",
            "vehicle_history_enabled": false
        },
        {
            "camera_id": "44d774d7-8bc1-46ca-bde4-ea422e7a0bf8",
            "cloud_retention": 0,
            "date_added": 1637788596,
            "device_retention": 30,
            "firmware": "Up to date v2025.03.28.690925-belson-4k",
            "firmware_update_schedule": "0,86400",
            "last_online": 1745720095,
            "local_ip": "192.168.4.128",
            "location": "Verkada HQ",
            "location_angle": 0.0,
            "location_lat": 37.56564,
            "location_lon": -122.32074,
            "mac": "E0:A7:00:10:82:95",
            "model": "CB61-E",
            "name": "Highland Gate exit",
            "people_history_enabled": true,
            "serial": "W9PR-DRA9-WY93",
            "site": "Highland Gate",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "status": "Live",
            "timezone": "America/Los_Angeles",
            "vehicle_history_enabled": true
        },
        {
            "camera_id": "600f3931-a414-48b4-b51f-fd4a954bc250",
            "cloud_retention": 0,
            "date_added": 1637788635,
            "device_retention": 30,
            "firmware": "Up to date v2025.03.28.690925-belson-4k",
            "firmware_update_schedule": "0,86400",
            "last_online": 1745720111,
            "local_ip": "192.168.4.117",
            "location": "Verkada HQ",
            "location_angle": 0.0,
            "location_lat": 37.56564,
            "location_lon": -122.32074,
            "mac": "E0:A7:00:10:7D:99",
            "model": "CB61-E",
            "name": "Highland Gate entrance ",
            "people_history_enabled": true,
            "serial": "W9PP-TF7K-X9XK",
            "site": "Highland Gate",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "status": "Live",
            "timezone": "America/Los_Angeles",
            "vehicle_history_enabled": true
        },
        {
            "camera_id": "67364fd9-556e-4923-9094-2873f9dc04ba",
            "cloud_retention": 0,
            "date_added": 1638308886,
            "device_retention": 30,
            "firmware": "Up to date v2025.03.28.690925-belson-4k",
            "firmware_update_schedule": "0,86400",
            "last_online": 1745720114,
            "local_ip": "192.168.1.59",
            "location": "Verkada HQ",
            "location_angle": 0.0,
            "location_lat": 37.56564,
            "location_lon": -122.32074,
            "mac": "E0:A7:00:10:7D:39",
            "model": "CB61-E",
            "name": "Main Gate Entrance",
            "people_history_enabled": true,
            "serial": "W9PP-PYXY-KXCD",
            "site": "Main Gate ",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "status": "Live",
            "timezone": "America/Los_Angeles",
            "vehicle_history_enabled": true
        },
        {
            "camera_id": "8c219867-9e7a-40e1-b19d-020f7458558c",
            "cloud_retention": 0,
            "date_added": 1639726183,
            "device_retention": 30,
            "firmware": "Up to date v2025.03.28.690925-belson-4k",
            "firmware_update_schedule": "0,86400",
            "last_online": 1745720109,
            "local_ip": "192.168.4.187",
            "location": "Encinitas, California",
            "location_angle": 0.0,
            "location_lat": 33.02476119995117,
            "location_lon": -117.19603729248047,
            "mac": "E0:A7:00:16:4E:F1",
            "model": "CB61-TE",
            "name": "Highland License Plate",
            "people_history_enabled": false,
            "serial": "MTFH-KHMN-QWQ6",
            "site": "Highland Gate",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "status": "Live",
            "timezone": "America/Los_Angeles",
            "vehicle_history_enabled": false
        },
        {
            "camera_id": "8efaf16a-b117-40e5-b3eb-506cc94ee5a2",
            "cloud_retention": 0,
            "date_added": 1638224462,
            "device_retention": 30,
            "firmware": "Up to date v2025.03.28.690925-belson-4k",
            "firmware_update_schedule": "0,86400",
            "last_online": 1745720111,
            "local_ip": "192.168.1.56",
            "location": "Verkada HQ",
            "location_angle": 0.0,
            "location_lat": 37.56564,
            "location_lon": -122.32074,
            "mac": "E0:A7:00:10:80:21",
            "model": "CB61-E",
            "name": "Main Gate Approaching",
            "people_history_enabled": true,
            "serial": "W9PQ-M4M7-RRC4",
            "site": "Main Gate ",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "status": "Live",
            "timezone": "America/Los_Angeles",
            "vehicle_history_enabled": true
        },
        {
            "camera_id": "ab34699a-038b-41b4-98b4-9d83055489b6",
            "cloud_retention": 0,
            "date_added": 1638299842,
            "device_retention": 30,
            "firmware": "Up to date v2025.03.28.690925-belson-4k",
            "firmware_update_schedule": "0,86400",
            "last_online": 1745720109,
            "local_ip": "192.168.1.57",
            "location": "Verkada HQ",
            "location_angle": 0.0,
            "location_lat": 37.56564,
            "location_lon": -122.32074,
            "mac": "E0:A7:00:10:7E:69",
            "model": "CB61-E",
            "name": "Main Gate Exit License Plates",
            "people_history_enabled": true,
            "serial": "W9PQ-6NKQ-6RTX",
            "site": "Main Gate ",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "status": "Live",
            "timezone": "America/Los_Angeles",
            "vehicle_history_enabled": false
        },
        {
            "camera_id": "d1e37446-ca48-4398-9243-49a99ea4bc80",
            "cloud_retention": 0,
            "date_added": 1733870594,
            "device_retention": 30,
            "firmware": "Up to date v2025.02.24.678095-bruce-4k-secure",
            "firmware_update_schedule": "0,86400",
            "last_online": 1745720069,
            "local_ip": "192.168.3.110",
            "location": "405 E 4th Ave, San Mateo, CA 94401, USA",
            "location_angle": 0.0,
            "location_lat": 37.5657216,
            "location_lon": -122.3207393,
            "mac": "E0:A7:00:2A:81:D1",
            "model": "CB62-E",
            "name": "Mesa Exit License Plate",
            "people_history_enabled": true,
            "serial": "3EW7-4G96-R777",
            "site": "Mesa Gate",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "status": "Live",
            "timezone": "America/Los_Angeles",
            "vehicle_history_enabled": false
        },
        {
            "camera_id": "f9cd473f-3794-4bee-825c-d1ae60d8e791",
            "cloud_retention": 0,
            "date_added": 1732054707,
            "device_retention": 30,
            "firmware": "Up to date v2025.02.24.678069-bruce-4k",
            "firmware_update_schedule": "0,86400",
            "last_online": 1745720103,
            "local_ip": "192.168.1.55",
            "location": "Escondido, CA, USA",
            "location_angle": 0.0,
            "location_lat": 33.1192068,
            "location_lon": -117.086421,
            "mac": "E0:A7:00:2A:7D:94",
            "model": "CB62-E",
            "name": "Main Gate License Plate ",
            "people_history_enabled": false,
            "serial": "AC7Y-6FXT-KCGN",
            "site": "Main Gate ",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "status": "Live",
            "timezone": "America/Los_Angeles",
            "vehicle_history_enabled": false
        }
    ],
    "next_page_token": null
}
2025-04-26 22:15:27,968 - __main__ - INFO - Successfully retrieved camera data (first page)
2025-04-26 22:15:27,970 - src_helix.api_utils - INFO - Generated JSON template: src_helix/api-json/test_cameras_api.json
PASS: Camera List

--------------------------------------------------------------------------------
Running Test: Access Events
Script: test_access_events_api.py
--------------------------------------------------------------------------------
  -> Using default history_days=1
--------------------------------------------------------------------------------
Running: python -m src_helix.test_access_events_api --log_level INFO --history_days 1
--------------------------------------------------------------------------------
2025-04-26 22:15:28,997 - __main__ - INFO - Successfully retrieved API token: v2_c9ab1e8...
2025-04-26 22:15:28,997 - __main__ - INFO - Querying access events for the last 1 days (from 2025-04-25 22:15:28 to 2025-04-26 22:15:28)
2025-04-26 22:15:28,997 - __main__ - INFO - Attempting to fetch access events from /events/v1/access

--- Access Events API Response from /events/v1/access ---
{
    "events": [
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "51ea6fc6-cbd0-4959-94fe-e2341d1fa844",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "51ea6fc6-cbd0-4959-94fe-e2341d1fa844"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:15:22Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "96c22eae-cd5b-45fc-b762-2ff79811440b",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "5DVR175",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "5DVR175",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "96c22eae-cd5b-45fc-b762-2ff79811440b"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:15:04Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "680a834c-2af8-4733-8be5-85c7aa6f4758",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9CBP500",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9CBP500",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "ae443d12-9380-49d7-8364-83ac18164678",
                "userInfo": {
                    "email": "katherinevillariasa@icloud.com",
                    "firstName": "Katherine",
                    "lastName": "Villariasa",
                    "name": "Katherine Villariasa",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "ae443d12-9380-49d7-8364-83ac18164678"
                },
                "userName": "Katherine Villariasa",
                "uuid": "680a834c-2af8-4733-8be5-85c7aa6f4758"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T02:10:49Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "e7707d40-4ddf-4323-869d-ffb89e02ce0e",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "remote_unlock_accepted",
                "userId": "9288df25-ff11-4f3b-8a2e-1e0452ac4922",
                "userInfo": {
                    "email": "svillariasa@icloud.com",
                    "firstName": "Steve",
                    "lastName": "Villariasa",
                    "name": "Steve Villariasa",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "9288df25-ff11-4f3b-8a2e-1e0452ac4922"
                },
                "userName": "Steve Villariasa",
                "uuid": "e7707d40-4ddf-4323-869d-ffb89e02ce0e"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T02:10:35Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "8a0b20be-ba78-4baf-b752-b14b513ec240",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "remote_unlock_accepted",
                "userId": "9288df25-ff11-4f3b-8a2e-1e0452ac4922",
                "userInfo": {
                    "email": "svillariasa@icloud.com",
                    "firstName": "Steve",
                    "lastName": "Villariasa",
                    "name": "Steve Villariasa",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "9288df25-ff11-4f3b-8a2e-1e0452ac4922"
                },
                "userName": "Steve Villariasa",
                "uuid": "8a0b20be-ba78-4baf-b752-b14b513ec240"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T02:10:28Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "99179a41-95d2-485e-aeac-7ac367913a9e",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "remote_unlock_accepted",
                "userId": "9288df25-ff11-4f3b-8a2e-1e0452ac4922",
                "userInfo": {
                    "email": "svillariasa@icloud.com",
                    "firstName": "Steve",
                    "lastName": "Villariasa",
                    "name": "Steve Villariasa",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "9288df25-ff11-4f3b-8a2e-1e0452ac4922"
                },
                "userName": "Steve Villariasa",
                "uuid": "99179a41-95d2-485e-aeac-7ac367913a9e"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T02:10:21Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "64e5a417-ca1f-48ab-afd7-6c2539907a67",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "6WTP420",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "6WTP420",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "64e5a417-ca1f-48ab-afd7-6c2539907a67"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:08:56Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "7f6d0873-383c-46c1-b1db-f90254ed093a",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "remote_unlock_accepted",
                "userId": "d025bccf-1369-4197-827c-1d13c9306163",
                "userInfo": {
                    "email": "abby.ramos27@gmail.com",
                    "firstName": "Abby",
                    "lastName": "Ramos",
                    "name": "Abby Ramos",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "d025bccf-1369-4197-827c-1d13c9306163"
                },
                "userName": "Abby Ramos",
                "uuid": "7f6d0873-383c-46c1-b1db-f90254ed093a"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-27T02:08:53Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "2c994d81-5ef3-4d1e-a86f-dc18a72c5bb9",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "d025bccf-1369-4197-827c-1d13c9306163",
                "userInfo": {
                    "email": "abby.ramos27@gmail.com",
                    "firstName": "Abby",
                    "lastName": "Ramos",
                    "name": "Abby Ramos",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "d025bccf-1369-4197-827c-1d13c9306163"
                },
                "userName": "Abby Ramos",
                "uuid": "2c994d81-5ef3-4d1e-a86f-dc18a72c5bb9"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:08:53Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "93a0e1cb-5be8-49cc-a9c0-174a5ecb8ae2",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "6WTP420",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "6WTP420",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "93a0e1cb-5be8-49cc-a9c0-174a5ecb8ae2"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:08:45Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "69f376f0-13a7-4233-b147-fe5715d4beb6",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "6WTP420",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "6WTP420",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "69f376f0-13a7-4233-b147-fe5715d4beb6"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:08:35Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "dd6ba9ac-d9a4-4ece-8bf9-5ca013b2bc1c",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "6WTP420",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "6WTP420",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "dd6ba9ac-d9a4-4ece-8bf9-5ca013b2bc1c"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:08:24Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "8cd18189-74b7-4dd2-93e6-1abfa371aaba",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "6WTP420",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "6WTP420",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "8cd18189-74b7-4dd2-93e6-1abfa371aaba"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:08:14Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "8c7771d1-9c3b-4a85-a424-f28f0933f78d",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "TP4201",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "TP4201",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "8c7771d1-9c3b-4a85-a424-f28f0933f78d"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:08:13Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "bdfbcfba-f345-42a1-866d-c4c9515a7a0b",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "TP4200",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "TP4200",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "bdfbcfba-f345-42a1-866d-c4c9515a7a0b"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:08:13Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "1dec951a-353e-409e-ae1b-ddf2fc3d1b32",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "4201",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "4201",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "1dec951a-353e-409e-ae1b-ddf2fc3d1b32"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:08:12Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "c98519a6-08ce-48e6-bd30-d91b08fa2981",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9PXD257",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9PXD257",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "88f033d9-7342-4cc4-a2e9-7e341ad1c6cf",
                "userInfo": {
                    "email": "helena.kim374@gmail.com",
                    "firstName": "Helena",
                    "lastName": "Kim",
                    "name": "Helena Kim",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "+17607056147",
                    "userId": "88f033d9-7342-4cc4-a2e9-7e341ad1c6cf"
                },
                "userName": "Helena Kim",
                "uuid": "c98519a6-08ce-48e6-bd30-d91b08fa2981"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:05:52Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "45ba0723-888c-419c-8f63-515efb085c66",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9PBM125",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9PBM125",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "3a593f3f-ad0c-4f49-b33c-4ad9f0220757",
                "userInfo": {
                    "email": "nlostetter99@gmail.com",
                    "firstName": "Nicholas",
                    "lastName": "Lostetter",
                    "name": "Nicholas Lostetter",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "3a593f3f-ad0c-4f49-b33c-4ad9f0220757"
                },
                "userName": "Nicholas Lostetter",
                "uuid": "45ba0723-888c-419c-8f63-515efb085c66"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:05:07Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "b31d6d15-5470-4d13-8637-20396da23271",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "6UAP937",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "6UAP937",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "88f033d9-7342-4cc4-a2e9-7e341ad1c6cf",
                "userInfo": {
                    "email": "helena.kim374@gmail.com",
                    "firstName": "Helena",
                    "lastName": "Kim",
                    "name": "Helena Kim",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "+17607056147",
                    "userId": "88f033d9-7342-4cc4-a2e9-7e341ad1c6cf"
                },
                "userName": "Helena Kim",
                "uuid": "b31d6d15-5470-4d13-8637-20396da23271"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:02:24Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "b733337b-7005-4dc7-8f3a-0c0adb0b33c6",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9RLN223",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9RLN223",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "d1aec312-99db-40a1-88f3-5d89a514d9ba",
                "userInfo": {
                    "email": "teamtlc@live.com",
                    "firstName": "Thomas",
                    "lastName": "Chung",
                    "name": "Thomas Chung",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "d1aec312-99db-40a1-88f3-5d89a514d9ba"
                },
                "userName": "Thomas Chung",
                "uuid": "b733337b-7005-4dc7-8f3a-0c0adb0b33c6"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T02:01:25Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "bfc15b3b-9bbc-4dcd-9bec-173e3c2de4d5",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "f4eee2e4d0433d907668d7b8060605a5be900db5c9b5a3457300ec4fd429c249",
                "lockdownInfo": null,
                "message": "BLE unlock attempt",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "f4eee2e4d0433d907668d7b8060605a5be900db5c9b5a3457300ec4fd429c249",
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "ble_unlock_attempt_accepted",
                "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c",
                "userInfo": {
                    "email": "edenlbergstrom@gmail.com",
                    "firstName": "Eden",
                    "lastName": "Bergstrom",
                    "name": "Eden Bergstrom",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c"
                },
                "userName": "Eden Bergstrom",
                "uuid": "bfc15b3b-9bbc-4dcd-9bec-173e3c2de4d5"
            },
            "event_type": "DOOR_BLE_UNLOCK_ATTEMPT_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-27T01:58:33Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "12b4be6c-3bbb-4b19-9626-7f4356db0c62",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "f4eee2e4d0433d907668d7b8060605a5be900db5c9b5a3457300ec4fd429c249",
                "lockdownInfo": null,
                "message": "BLE unlock attempt",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "f4eee2e4d0433d907668d7b8060605a5be900db5c9b5a3457300ec4fd429c249",
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "ble_unlock_attempt_accepted",
                "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c",
                "userInfo": {
                    "email": "edenlbergstrom@gmail.com",
                    "firstName": "Eden",
                    "lastName": "Bergstrom",
                    "name": "Eden Bergstrom",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c"
                },
                "userName": "Eden Bergstrom",
                "uuid": "12b4be6c-3bbb-4b19-9626-7f4356db0c62"
            },
            "event_type": "DOOR_BLE_UNLOCK_ATTEMPT_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-27T01:58:30Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "9d39c4b7-5f4a-4447-933d-103f3adfc24a",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "f4eee2e4d0433d907668d7b8060605a5be900db5c9b5a3457300ec4fd429c249",
                "lockdownInfo": null,
                "message": "BLE unlock attempt",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "f4eee2e4d0433d907668d7b8060605a5be900db5c9b5a3457300ec4fd429c249",
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "ble_unlock_attempt_accepted",
                "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c",
                "userInfo": {
                    "email": "edenlbergstrom@gmail.com",
                    "firstName": "Eden",
                    "lastName": "Bergstrom",
                    "name": "Eden Bergstrom",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c"
                },
                "userName": "Eden Bergstrom",
                "uuid": "9d39c4b7-5f4a-4447-933d-103f3adfc24a"
            },
            "event_type": "DOOR_BLE_UNLOCK_ATTEMPT_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-27T01:58:28Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "2113ef12-7007-48e0-94b5-fa920c37eb65",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "86e1d26e-73bb-44e6-86c3-8193afa9e2ba",
                "userInfo": {
                    "email": "robert.tahiry@brightstarcare.com",
                    "firstName": "Robert",
                    "lastName": "Tahiry",
                    "name": "Robert Tahiry",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "86e1d26e-73bb-44e6-86c3-8193afa9e2ba"
                },
                "userName": "Robert Tahiry",
                "uuid": "2113ef12-7007-48e0-94b5-fa920c37eb65"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:55:26Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "dcf9755e-fd90-413f-a30a-6e5cb55b0dd8",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7AYM395",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7AYM395",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "dcf9755e-fd90-413f-a30a-6e5cb55b0dd8"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:53:46Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "acc62fdf-dd89-493c-b907-ae2cea2fa40c",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "1SKID0",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "1SKID0",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "af2448bd-6e24-40f9-a4bd-09445614fe19",
                "userInfo": {
                    "email": "cedarrockventures@gmail.com",
                    "firstName": "Martin (1SKIDO)",
                    "lastName": "Wronski",
                    "name": "Martin (1SKIDO) Wronski",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "af2448bd-6e24-40f9-a4bd-09445614fe19"
                },
                "userName": "Martin (1SKIDO) Wronski",
                "uuid": "acc62fdf-dd89-493c-b907-ae2cea2fa40c"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:53:30Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "f2dc41e9-781b-4371-bcc0-bd8b295c67cc",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "26|57509",
                "lockdownInfo": null,
                "message": "Keycard Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "00001101011100000101001011",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "keycard_entered_accepted",
                "userId": "af2448bd-6e24-40f9-a4bd-09445614fe19",
                "userInfo": {
                    "email": "cedarrockventures@gmail.com",
                    "firstName": "Martin (1SKIDO)",
                    "lastName": "Wronski",
                    "name": "Martin (1SKIDO) Wronski",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "af2448bd-6e24-40f9-a4bd-09445614fe19"
                },
                "userName": "Martin (1SKIDO) Wronski",
                "uuid": "f2dc41e9-781b-4371-bcc0-bd8b295c67cc"
            },
            "event_type": "DOOR_KEYCARD_ENTERED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:53:27Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "aaa25408-0d01-4efd-8bb0-5a3b1bb8c697",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7AYM395",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7AYM395",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "aaa25408-0d01-4efd-8bb0-5a3b1bb8c697"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:53:16Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "fae008f7-789a-485a-9ff6-0c875d0acbc9",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7AYM395",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7AYM395",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "fae008f7-789a-485a-9ff6-0c875d0acbc9"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:53:06Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "a833f4cf-9a70-4c0f-a00f-3a5ccbb83c25",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "AE924V",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "AE924V",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "a833f4cf-9a70-4c0f-a00f-3a5ccbb83c25"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:46:02Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "24a4f440-b02d-45bc-bd2b-37813b178fcd",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "1AE924V",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "1AE924V",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "90f75ebe-a2b1-45c8-9b3d-97d51677e53c",
                "userInfo": {
                    "email": "kaxonknievel@gmail.com",
                    "firstName": " Jaxon Knievel tenant",
                    "lastName": "Mary Kate Lowe",
                    "name": " Jaxon Knievel tenant Mary Kate Lowe",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "90f75ebe-a2b1-45c8-9b3d-97d51677e53c"
                },
                "userName": " Jaxon Knievel tenant Mary Kate Lowe",
                "uuid": "24a4f440-b02d-45bc-bd2b-37813b178fcd"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:46:02Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "5a3a9481-985b-46cc-b111-8e5c2b05e815",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "17659H3",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "17659H3",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "3bdb3c3b-f6fe-4dc5-a307-1775e09489dd",
                "userInfo": {
                    "email": "sam@vantedgeplans.com",
                    "firstName": "Hussam",
                    "lastName": "Elfarra",
                    "name": "Hussam Elfarra",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "3bdb3c3b-f6fe-4dc5-a307-1775e09489dd"
                },
                "userName": "Hussam Elfarra",
                "uuid": "5a3a9481-985b-46cc-b111-8e5c2b05e815"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:42:38Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "05c7fb45-0ba5-487b-add5-e556e2344267",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9GBU330",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9GBU330",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "05c7fb45-0ba5-487b-add5-e556e2344267"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:42:14Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "7e53ee26-4587-4568-b83b-1199c2a8740d",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9H0H039",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9H0H039",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "7e53ee26-4587-4568-b83b-1199c2a8740d"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:42:10Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "a0833986-5b29-42bb-9cd3-bb144bc70281",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "d0832aa9-99fd-428c-88c6-d4dbd73d567c",
                "userInfo": {
                    "email": "tahirysumaya@gmail.com",
                    "firstName": "Sumaya",
                    "lastName": "Tahiry",
                    "name": "Sumaya Tahiry",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "d0832aa9-99fd-428c-88c6-d4dbd73d567c"
                },
                "userName": "Sumaya Tahiry",
                "uuid": "a0833986-5b29-42bb-9cd3-bb144bc70281"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:42:05Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "8adc2340-77fd-41f7-be36-41c807149a48",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9GBU330",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9GBU330",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "8adc2340-77fd-41f7-be36-41c807149a48"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:42:03Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "4c35b015-1dec-4352-be20-96d723785258",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9H0H039",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9H0H039",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "4c35b015-1dec-4352-be20-96d723785258"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:41:59Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "34012629-809f-4a37-b5c8-505bb261456a",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "65de5d03-a05b-41a8-802d-a8813f110625",
                "userInfo": {
                    "email": "tahirymadina@gmail.com",
                    "firstName": "Madina",
                    "lastName": "Tahiry",
                    "name": "Madina Tahiry",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "65de5d03-a05b-41a8-802d-a8813f110625"
                },
                "userName": "Madina Tahiry",
                "uuid": "34012629-809f-4a37-b5c8-505bb261456a"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:39:54Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "dac7eb8a-3e5d-4e56-9d14-f4f588e8bfd2",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "65de5d03-a05b-41a8-802d-a8813f110625",
                "userInfo": {
                    "email": "tahirymadina@gmail.com",
                    "firstName": "Madina",
                    "lastName": "Tahiry",
                    "name": "Madina Tahiry",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "65de5d03-a05b-41a8-802d-a8813f110625"
                },
                "userName": "Madina Tahiry",
                "uuid": "dac7eb8a-3e5d-4e56-9d14-f4f588e8bfd2"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:39:52Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "8ecb7428-1ad0-4da3-9747-7ad833fdbe72",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9HYB970",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9HYB970",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "8ecb7428-1ad0-4da3-9747-7ad833fdbe72"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:39:51Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "6a7862d0-8dac-494b-b215-b4d67443568a",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9HYB970",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9HYB970",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "6a7862d0-8dac-494b-b215-b4d67443568a"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:39:40Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "a821cba2-0bd9-4a13-b99e-1fb203676f8a",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "HYB970",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "HYB970",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "a821cba2-0bd9-4a13-b99e-1fb203676f8a"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:39:40Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "80feba87-c93c-4744-a75f-f4e24f3c621a",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "remote_unlock_accepted",
                "userId": "b02aab22-d059-4813-af21-0a3e718dba51",
                "userInfo": {
                    "email": "matthewanand@gmail.com",
                    "firstName": "Matthew ",
                    "lastName": "Anand",
                    "name": "Matthew  Anand",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "b02aab22-d059-4813-af21-0a3e718dba51"
                },
                "userName": "Matthew  Anand",
                "uuid": "80feba87-c93c-4744-a75f-f4e24f3c621a"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-27T01:38:19Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "e7a16daf-1c97-427c-9032-407df24c8127",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "remote_unlock_accepted",
                "userId": "b02aab22-d059-4813-af21-0a3e718dba51",
                "userInfo": {
                    "email": "matthewanand@gmail.com",
                    "firstName": "Matthew ",
                    "lastName": "Anand",
                    "name": "Matthew  Anand",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "b02aab22-d059-4813-af21-0a3e718dba51"
                },
                "userName": "Matthew  Anand",
                "uuid": "e7a16daf-1c97-427c-9032-407df24c8127"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-27T01:38:16Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "361b1c2c-0759-44d5-9408-29d1582e1de7",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "remote_unlock_accepted",
                "userId": "b02aab22-d059-4813-af21-0a3e718dba51",
                "userInfo": {
                    "email": "matthewanand@gmail.com",
                    "firstName": "Matthew ",
                    "lastName": "Anand",
                    "name": "Matthew  Anand",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "b02aab22-d059-4813-af21-0a3e718dba51"
                },
                "userName": "Matthew  Anand",
                "uuid": "361b1c2c-0759-44d5-9408-29d1582e1de7"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-27T01:38:12Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "f57b5339-271b-4de6-8867-d7f181bf2941",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "4XFT021",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "4XFT021",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c",
                "userInfo": {
                    "email": "edenlbergstrom@gmail.com",
                    "firstName": "Eden",
                    "lastName": "Bergstrom",
                    "name": "Eden Bergstrom",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c"
                },
                "userName": "Eden Bergstrom",
                "uuid": "f57b5339-271b-4de6-8867-d7f181bf2941"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T01:37:29Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "3dd294c0-9aba-4592-9ef1-3cd7a182bdab",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "4XFT021",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "4XFT021",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c",
                "userInfo": {
                    "email": "edenlbergstrom@gmail.com",
                    "firstName": "Eden",
                    "lastName": "Bergstrom",
                    "name": "Eden Bergstrom",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c"
                },
                "userName": "Eden Bergstrom",
                "uuid": "3dd294c0-9aba-4592-9ef1-3cd7a182bdab"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T01:37:19Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "3f9a1bd0-3da1-4acc-b8ca-c3fd729afdf5",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TNC370",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TNC370",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "3f9a1bd0-3da1-4acc-b8ca-c3fd729afdf5"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:36:21Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "d119d9c7-8007-4bc6-9148-671d0002d617",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "86e1d26e-73bb-44e6-86c3-8193afa9e2ba",
                "userInfo": {
                    "email": "robert.tahiry@brightstarcare.com",
                    "firstName": "Robert",
                    "lastName": "Tahiry",
                    "name": "Robert Tahiry",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "86e1d26e-73bb-44e6-86c3-8193afa9e2ba"
                },
                "userName": "Robert Tahiry",
                "uuid": "d119d9c7-8007-4bc6-9148-671d0002d617"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:36:19Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "83e8fb7f-6283-4d99-a06b-39e11cbfb5cc",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TNC370",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TNC370",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "83e8fb7f-6283-4d99-a06b-39e11cbfb5cc"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:36:11Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "437d3675-664d-4126-a797-cb94e4031552",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TNC370",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TNC370",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "437d3675-664d-4126-a797-cb94e4031552"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:36:00Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "23f63f99-2b3d-43e5-8ca3-02f5b828fe1f",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TNC370",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TNC370",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "23f63f99-2b3d-43e5-8ca3-02f5b828fe1f"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:35:50Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "7c222dde-1e2a-4882-9240-71524c9e14ad",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TNC370",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TNC370",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "7c222dde-1e2a-4882-9240-71524c9e14ad"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:35:39Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "975dd023-99ea-4489-9088-1df37255c70c",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TNC370",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TNC370",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "975dd023-99ea-4489-9088-1df37255c70c"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:35:29Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "901753b3-c71c-4a23-8266-5ca6e15fe6c9",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TNC370",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TNC370",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "901753b3-c71c-4a23-8266-5ca6e15fe6c9"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:35:18Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "2608e2fa-e6ec-41e7-b7fc-61f88010352c",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TNC370",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TNC370",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "2608e2fa-e6ec-41e7-b7fc-61f88010352c"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:35:08Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "83d626f7-4b81-4237-8693-4ca1a690fcf9",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TNC370",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TNC370",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "83d626f7-4b81-4237-8693-4ca1a690fcf9"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:34:57Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "eb622e86-6ce4-4a69-87d5-2656ad59db42",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c",
                "userInfo": {
                    "email": "edenlbergstrom@gmail.com",
                    "firstName": "Eden",
                    "lastName": "Bergstrom",
                    "name": "Eden Bergstrom",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c"
                },
                "userName": "Eden Bergstrom",
                "uuid": "eb622e86-6ce4-4a69-87d5-2656ad59db42"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:29:40Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "e03bbffe-0e8b-493f-bbd3-7e8c708aa0c1",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9BDP897",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9BDP897",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "e03bbffe-0e8b-493f-bbd3-7e8c708aa0c1"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:28:54Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "f6bae97c-fe29-43ff-951f-0524ed2c8dbf",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7aea2a2e8e063fb061825c23c0c2eff208ec59dec8eb0f87caea261dc63bb03f",
                "lockdownInfo": null,
                "message": "BLE unlock attempt",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7aea2a2e8e063fb061825c23c0c2eff208ec59dec8eb0f87caea261dc63bb03f",
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "ble_unlock_attempt_accepted",
                "userId": "ea8f74fe-cc83-49e6-9012-701aa9253268",
                "userInfo": {
                    "email": "jsanthoff@orioncable.com",
                    "firstName": "John Santhoff",
                    "lastName": "Orion Cable",
                    "name": "John Santhoff Orion Cable",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "ea8f74fe-cc83-49e6-9012-701aa9253268"
                },
                "userName": "John Santhoff Orion Cable",
                "uuid": "f6bae97c-fe29-43ff-951f-0524ed2c8dbf"
            },
            "event_type": "DOOR_BLE_UNLOCK_ATTEMPT_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-27T01:28:53Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "a2bbc4f4-b56a-4886-b687-c3ca79aae7a3",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7aea2a2e8e063fb061825c23c0c2eff208ec59dec8eb0f87caea261dc63bb03f",
                "lockdownInfo": null,
                "message": "BLE unlock attempt",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7aea2a2e8e063fb061825c23c0c2eff208ec59dec8eb0f87caea261dc63bb03f",
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "ble_unlock_attempt_accepted",
                "userId": "ea8f74fe-cc83-49e6-9012-701aa9253268",
                "userInfo": {
                    "email": "jsanthoff@orioncable.com",
                    "firstName": "John Santhoff",
                    "lastName": "Orion Cable",
                    "name": "John Santhoff Orion Cable",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "ea8f74fe-cc83-49e6-9012-701aa9253268"
                },
                "userName": "John Santhoff Orion Cable",
                "uuid": "a2bbc4f4-b56a-4886-b687-c3ca79aae7a3"
            },
            "event_type": "DOOR_BLE_UNLOCK_ATTEMPT_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-27T01:28:51Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "2964ab10-6e4c-40f3-940a-b7f6058d1714",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "fe3f78b7-aece-46df-bcc8-05ff557c8300",
                "userInfo": {
                    "email": "batoul.tahiry@brightstarcare.com",
                    "firstName": "Batoul",
                    "lastName": "Tahiry",
                    "name": "Batoul Tahiry",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "fe3f78b7-aece-46df-bcc8-05ff557c8300"
                },
                "userName": "Batoul Tahiry",
                "uuid": "2964ab10-6e4c-40f3-940a-b7f6058d1714"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:28:48Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "650c0546-4fa7-41b2-93c7-f2e3a7aa6591",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7aea2a2e8e063fb061825c23c0c2eff208ec59dec8eb0f87caea261dc63bb03f",
                "lockdownInfo": null,
                "message": "BLE unlock attempt",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7aea2a2e8e063fb061825c23c0c2eff208ec59dec8eb0f87caea261dc63bb03f",
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "ble_unlock_attempt_accepted",
                "userId": "ea8f74fe-cc83-49e6-9012-701aa9253268",
                "userInfo": {
                    "email": "jsanthoff@orioncable.com",
                    "firstName": "John Santhoff",
                    "lastName": "Orion Cable",
                    "name": "John Santhoff Orion Cable",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "ea8f74fe-cc83-49e6-9012-701aa9253268"
                },
                "userName": "John Santhoff Orion Cable",
                "uuid": "650c0546-4fa7-41b2-93c7-f2e3a7aa6591"
            },
            "event_type": "DOOR_BLE_UNLOCK_ATTEMPT_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-27T01:28:48Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "cfe5d377-02b1-4979-aaaf-0c483f8bb29a",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9BDP897",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9BDP897",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "cfe5d377-02b1-4979-aaaf-0c483f8bb29a"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:28:44Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "eefcd5ed-2e38-48d3-9ac4-650f9f5839df",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9BDP897",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9BDP897",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "eefcd5ed-2e38-48d3-9ac4-650f9f5839df"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:28:33Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "9e330b8c-2231-4a29-8b95-e51368f83dd4",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9MED309",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9MED309",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "9e330b8c-2231-4a29-8b95-e51368f83dd4"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:26:31Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "1cd1974b-367b-45f9-9ea5-d10d785de767",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "2b300b90-cbba-47ea-80ef-ca69a62d7bca",
                "userInfo": {
                    "email": "kathleendelmastro3@gmail.com",
                    "firstName": "Kathleen",
                    "lastName": "Delmastro",
                    "name": "Kathleen Delmastro",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "2b300b90-cbba-47ea-80ef-ca69a62d7bca"
                },
                "userName": "Kathleen Delmastro",
                "uuid": "1cd1974b-367b-45f9-9ea5-d10d785de767"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:26:29Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "6c299c2b-9b4a-4af8-904d-c2b5e3b97883",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "5FE1407",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "5FE1407",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "6c299c2b-9b4a-4af8-904d-c2b5e3b97883"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:25:37Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "76dc949c-a1b9-4255-96a1-e61d726f7471",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "b42afbaa-aa91-425b-9ef7-5e17dbbc5bc0",
                "userInfo": {
                    "email": "kelley0503@msn.com",
                    "firstName": "Kelley",
                    "lastName": "SCUTELNICU",
                    "name": "Kelley SCUTELNICU",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "b42afbaa-aa91-425b-9ef7-5e17dbbc5bc0"
                },
                "userName": "Kelley SCUTELNICU",
                "uuid": "76dc949c-a1b9-4255-96a1-e61d726f7471"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:24:44Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "f0acf74e-83d3-43e7-9135-21319ef2748b",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "5VSL622",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "5VSL622",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "f0acf74e-83d3-43e7-9135-21319ef2748b"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:24:10Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "39ed39a1-5991-4893-8e0e-dd28185aabd2",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "5VSL622",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "5VSL622",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "39ed39a1-5991-4893-8e0e-dd28185aabd2"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:23:59Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "911188ce-4c43-4788-b173-15d937cd78ac",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "5VSL622",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "5VSL622",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "911188ce-4c43-4788-b173-15d937cd78ac"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:23:49Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "95c62dc4-87a9-4744-9a37-ae23b27ab982",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "5VSL622",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "5VSL622",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "95c62dc4-87a9-4744-9a37-ae23b27ab982"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:23:38Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "e76d1200-f25e-4b70-b2e8-a5d8a907507f",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "5VSL622",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "5VSL622",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "e76d1200-f25e-4b70-b2e8-a5d8a907507f"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:23:28Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "421cbb82-7814-4dc6-a524-28e60d0e6bae",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9DZD206",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9DZD206",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "0895cbd2-ab57-4b3b-8b17-7a768ca996fa",
                "userInfo": {
                    "email": "jaimeramirez59@icloud.com",
                    "firstName": "Jaime",
                    "lastName": "Ramirez",
                    "name": "Jaime Ramirez",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "0895cbd2-ab57-4b3b-8b17-7a768ca996fa"
                },
                "userName": "Jaime Ramirez",
                "uuid": "421cbb82-7814-4dc6-a524-28e60d0e6bae"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:23:20Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "0138fa5c-31bd-4621-ae45-0396b9efdef9",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8ZWN343",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8ZWN343",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "0138fa5c-31bd-4621-ae45-0396b9efdef9"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T01:10:26Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "4ae9826e-4c77-4392-a0e7-a25e6062d4e8",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "1AE924V",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "1AE924V",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "90f75ebe-a2b1-45c8-9b3d-97d51677e53c",
                "userInfo": {
                    "email": "kaxonknievel@gmail.com",
                    "firstName": " Jaxon Knievel tenant",
                    "lastName": "Mary Kate Lowe",
                    "name": " Jaxon Knievel tenant Mary Kate Lowe",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "90f75ebe-a2b1-45c8-9b3d-97d51677e53c"
                },
                "userName": " Jaxon Knievel tenant Mary Kate Lowe",
                "uuid": "4ae9826e-4c77-4392-a0e7-a25e6062d4e8"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:07:23Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "1e70e3fb-2095-4204-95cb-49bc6ec875a3",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "1e70e3fb-2095-4204-95cb-49bc6ec875a3"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:03:09Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "0f4aa611-5072-453d-9bbd-dc4748cda6a0",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "17bdfcdb-05ff-4387-97cf-4cc8e1dafe42",
                "userInfo": {
                    "email": "dawnkorinek@gmail.com",
                    "firstName": "Dawn",
                    "lastName": "Fuller",
                    "name": "Dawn Fuller",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "17bdfcdb-05ff-4387-97cf-4cc8e1dafe42"
                },
                "userName": "Dawn Fuller",
                "uuid": "0f4aa611-5072-453d-9bbd-dc4748cda6a0"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:03:03Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "bd420a98-6188-40a0-963c-4e88c4ca8195",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "bd420a98-6188-40a0-963c-4e88c4ca8195"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:02:59Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "df22434b-ee8d-4016-bb0f-6e687f2edacf",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "df22434b-ee8d-4016-bb0f-6e687f2edacf"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:02:48Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "53fc7e4f-805f-494b-8ecf-1f24d13ed34b",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "53fc7e4f-805f-494b-8ecf-1f24d13ed34b"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:02:37Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "e834b36b-0042-40fc-bbf9-31512f28b91b",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "e834b36b-0042-40fc-bbf9-31512f28b91b"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:02:27Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "2dcbdb7f-a314-49f1-865d-1c5e4e4baa46",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "2dcbdb7f-a314-49f1-865d-1c5e4e4baa46"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:02:16Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "53975d50-6773-4ddf-ba47-3c083384cc3c",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "53975d50-6773-4ddf-ba47-3c083384cc3c"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:02:06Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "f3aab462-966b-49ad-ad98-07f0a9565667",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "f3aab462-966b-49ad-ad98-07f0a9565667"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:01:55Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "433f8dd8-0044-4e6d-b097-df61589c9678",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "433f8dd8-0044-4e6d-b097-df61589c9678"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:01:45Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "72dec73f-6988-4b9a-bfc8-e30f2a7a1202",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "72dec73f-6988-4b9a-bfc8-e30f2a7a1202"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:01:34Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "eee82b04-5f97-47bb-9ed5-750c42fb58a4",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "eee82b04-5f97-47bb-9ed5-750c42fb58a4"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:01:24Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "c0dfe672-9b6e-460b-99f0-09c9f9e1145e",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8141",
                "lockdownInfo": null,
                "message": "Code Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8141",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "code_entered_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "c0dfe672-9b6e-460b-99f0-09c9f9e1145e"
            },
            "event_type": "DOOR_CODE_ENTERED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:01:15Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "cb07850a-28fb-4f1a-b301-926495020f09",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "cb07850a-28fb-4f1a-b301-926495020f09"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:01:13Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "12d5bc30-0620-468e-ab7b-b647c1da424c",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "",
                "lockdownInfo": null,
                "message": "Code Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "code_entered_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "12d5bc30-0620-468e-ab7b-b647c1da424c"
            },
            "event_type": "DOOR_CODE_ENTERED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:01:11Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "134604e4-6066-4dcf-83d4-6d569090219b",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "134604e4-6066-4dcf-83d4-6d569090219b"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:01:03Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "069e0b65-fe50-4080-8344-74c6c72f527f",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "069e0b65-fe50-4080-8344-74c6c72f527f"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:00:52Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "40fd97b1-cb47-4b36-a03b-97a2dded3227",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FYY560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FYY560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "40fd97b1-cb47-4b36-a03b-97a2dded3227"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:00:42Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "4ba1b6b0-b8dc-4b0b-adc0-5e264238d6b8",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "Y560",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "Y560",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "4ba1b6b0-b8dc-4b0b-adc0-5e264238d6b8"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T01:00:42Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "96144604-f07f-495d-abc0-39313a64ad0a",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "6NGN094",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "6NGN094",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "36f989ba-831d-42ab-9d57-c1a227a62664",
                "userInfo": {
                    "email": "Arielsbergstrom@icloud.com",
                    "firstName": "Ariel",
                    "lastName": "Bergstrom",
                    "name": "Ariel Bergstrom",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "36f989ba-831d-42ab-9d57-c1a227a62664"
                },
                "userName": "Ariel Bergstrom",
                "uuid": "96144604-f07f-495d-abc0-39313a64ad0a"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:58:58Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "8ae72d38-13fe-4bb7-a719-02927f1bba9a",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "6NGN094",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "6NGN094",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "36f989ba-831d-42ab-9d57-c1a227a62664",
                "userInfo": {
                    "email": "Arielsbergstrom@icloud.com",
                    "firstName": "Ariel",
                    "lastName": "Bergstrom",
                    "name": "Ariel Bergstrom",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "36f989ba-831d-42ab-9d57-c1a227a62664"
                },
                "userName": "Ariel Bergstrom",
                "uuid": "8ae72d38-13fe-4bb7-a719-02927f1bba9a"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:58:48Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "5e799c86-94d1-4f31-9528-e236e38d0a9f",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9EYL463",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9EYL463",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "5e799c86-94d1-4f31-9528-e236e38d0a9f"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:58:16Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "9ffeed79-c7c5-4f40-995a-1e93ac5c0552",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9EYL463",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9EYL463",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "9ffeed79-c7c5-4f40-995a-1e93ac5c0552"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:58:06Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "cfa1b493-6460-4dc4-af6a-0b8598cd64a5",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9EYL",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9EYL",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "cfa1b493-6460-4dc4-af6a-0b8598cd64a5"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:58:06Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "65c593eb-b608-47ac-9ec9-fe1dab2993d1",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9EYL4",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9EYL4",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "65c593eb-b608-47ac-9ec9-fe1dab2993d1"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:58:06Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "4620dd2c-38fb-425a-9bbe-fc6b029e6f68",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9EYL46",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9EYL46",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "4620dd2c-38fb-425a-9bbe-fc6b029e6f68"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:58:06Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "a84579fb-3f6e-47e2-8601-984d62376a72",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "remote_unlock_accepted",
                "userId": "097de7ef-b8ca-4550-bf4f-b12e9f2288fb",
                "userInfo": {
                    "email": "kimydebow@icloud.com",
                    "firstName": "Kim",
                    "lastName": "DeBow",
                    "name": "Kim DeBow",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "097de7ef-b8ca-4550-bf4f-b12e9f2288fb"
                },
                "userName": "Kim DeBow",
                "uuid": "a84579fb-3f6e-47e2-8601-984d62376a72"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:58:02Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "7979e1df-4bbe-4f46-9ced-da809948afa9",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8JGC015",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8JGC015",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "66d560ac-7866-4f07-a68f-b80bea9c7a47",
                "userInfo": {
                    "email": "izzyhermosillo999@gmail.com",
                    "firstName": "Izzy",
                    "lastName": "Hermosillo",
                    "name": "Izzy Hermosillo",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "66d560ac-7866-4f07-a68f-b80bea9c7a47"
                },
                "userName": "Izzy Hermosillo",
                "uuid": "7979e1df-4bbe-4f46-9ced-da809948afa9"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:56:33Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "826caf8e-413e-4e19-9d10-8ff33e7b9905",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "24917V3",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "24917V3",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "bf3c7281-6911-40b0-8d99-4fad6c4eecd5",
                "userInfo": {
                    "email": null,
                    "firstName": "Connor",
                    "lastName": "McManigal",
                    "name": "Connor McManigal",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "bf3c7281-6911-40b0-8d99-4fad6c4eecd5"
                },
                "userName": "Connor McManigal",
                "uuid": "826caf8e-413e-4e19-9d10-8ff33e7b9905"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:55:13Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "fd2cc2b1-7f24-468d-a6ab-27cc963684f9",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "DCE1983",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "DCE1983",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "6a674d9f-be89-49bb-9616-e01aecec60e9",
                "userInfo": {
                    "email": "sleepdoc2@me.com",
                    "firstName": "Rick",
                    "lastName": "Engel",
                    "name": "Rick Engel",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "6a674d9f-be89-49bb-9616-e01aecec60e9"
                },
                "userName": "Rick Engel",
                "uuid": "fd2cc2b1-7f24-468d-a6ab-27cc963684f9"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:53:04Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "51c7d3d9-7317-4b79-9d43-d2f5c8181c27",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9EDT604",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9EDT604",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "b4e78c21-8dea-4c27-99a9-c67c719bafa6",
                "userInfo": {
                    "email": "jameskshin2000@yahoo.com",
                    "firstName": "James",
                    "lastName": "Shin",
                    "name": "James Shin",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "b4e78c21-8dea-4c27-99a9-c67c719bafa6"
                },
                "userName": "James Shin",
                "uuid": "51c7d3d9-7317-4b79-9d43-d2f5c8181c27"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:52:05Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "fb20ca49-16a8-4b85-aa87-0d8d36c44685",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "fb20ca49-16a8-4b85-aa87-0d8d36c44685"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:45Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "0bf1de24-610d-4194-960f-5183475b4171",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "0bf1de24-610d-4194-960f-5183475b4171"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:43Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "afb4a02a-d5cc-4fac-b49d-d6f2c30b60e5",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "afb4a02a-d5cc-4fac-b49d-d6f2c30b60e5"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:40Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "fa5b63ae-2d1f-4164-9e95-c12949beee52",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "fa5b63ae-2d1f-4164-9e95-c12949beee52"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:32Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "140f942f-0d27-494b-9b74-cc035a744098",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "140f942f-0d27-494b-9b74-cc035a744098"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:30Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "8e865838-7f65-43ca-944f-6a37cb1e222d",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "8e865838-7f65-43ca-944f-6a37cb1e222d"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:27Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "7eb1edc8-1b63-4a83-9a67-22d50a01beda",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "7eb1edc8-1b63-4a83-9a67-22d50a01beda"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:23Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "dd55a73e-f440-44cc-b6ce-f5b1bbc8e811",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "5MLX532",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "5MLX532",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "dd55a73e-f440-44cc-b6ce-f5b1bbc8e811"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:22Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "aa01d795-a992-44ac-a4e0-a895c3c6c1e9",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "aa01d795-a992-44ac-a4e0-a895c3c6c1e9"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:21Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "7aff949b-c460-49af-be71-835144b2557a",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "7aff949b-c460-49af-be71-835144b2557a"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:18Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "087611cf-81ae-438f-86bd-8e802d101b43",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "087611cf-81ae-438f-86bd-8e802d101b43"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:16Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "4004b39a-a5d7-4741-b6d2-f606a0a832e1",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "5MLX532",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "5MLX532",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "4004b39a-a5d7-4741-b6d2-f606a0a832e1"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:50:11Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "e732c5ec-47cd-4384-99e3-58222a77f6e7",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c",
                "userInfo": {
                    "email": "edenlbergstrom@gmail.com",
                    "firstName": "Eden",
                    "lastName": "Bergstrom",
                    "name": "Eden Bergstrom",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "f653d5d8-1172-483a-b8b3-2f23d0a47e3c"
                },
                "userName": "Eden Bergstrom",
                "uuid": "e732c5ec-47cd-4384-99e3-58222a77f6e7"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:46:09Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "d88218de-3989-48dd-a7dd-690fab918d52",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9MPX218",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9MPX218",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "d88218de-3989-48dd-a7dd-690fab918d52"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:29:33Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "4090993e-df02-43ee-b16e-71eac9edc749",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9HSH993",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9HSH993",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "d0832aa9-99fd-428c-88c6-d4dbd73d567c",
                "userInfo": {
                    "email": "tahirysumaya@gmail.com",
                    "firstName": "Sumaya",
                    "lastName": "Tahiry",
                    "name": "Sumaya Tahiry",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "d0832aa9-99fd-428c-88c6-d4dbd73d567c"
                },
                "userName": "Sumaya Tahiry",
                "uuid": "4090993e-df02-43ee-b16e-71eac9edc749"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:17:47Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "34b8a437-abb5-4338-8439-9fea74e3b5e8",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "35600D4",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "35600D4",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "2d34ed50-ac75-4c35-8804-5650db2dd276",
                "userInfo": {
                    "email": "chris@vintagecellars.com",
                    "firstName": "Christopher",
                    "lastName": "Noel",
                    "name": "Christopher Noel",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "+16193978965",
                    "userId": "2d34ed50-ac75-4c35-8804-5650db2dd276"
                },
                "userName": "Christopher Noel",
                "uuid": "34b8a437-abb5-4338-8439-9fea74e3b5e8"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:06:49Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "8adab318-d6b3-4e25-ad27-c91918567b13",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "29|28169",
                "lockdownInfo": null,
                "message": "Keycard Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "00001110101101110000010010",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "keycard_entered_accepted",
                "userId": "c5822ed4-2047-4e64-acc6-d8cc15877b88",
                "userInfo": {
                    "email": "getse@vintagecellars.com",
                    "firstName": "Paola",
                    "lastName": "Noel",
                    "name": "Paola Noel",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "+16193724467",
                    "userId": "c5822ed4-2047-4e64-acc6-d8cc15877b88"
                },
                "userName": "Paola Noel",
                "uuid": "8adab318-d6b3-4e25-ad27-c91918567b13"
            },
            "event_type": "DOOR_KEYCARD_ENTERED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:06:35Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "1d875090-ad52-4b6a-8d45-051c7581e784",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7SMB304",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7SMB304",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "0e239001-88ce-4a59-bf4a-a0bcd723efc8",
                "userInfo": {
                    "email": "marsham760@gmail.com",
                    "firstName": "Marsha ",
                    "lastName": "Michael",
                    "name": "Marsha  Michael",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "0e239001-88ce-4a59-bf4a-a0bcd723efc8"
                },
                "userName": "Marsha  Michael",
                "uuid": "1d875090-ad52-4b6a-8d45-051c7581e784"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-27T00:04:05Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "cabddc9e-1f4a-4a9a-8abf-32598e43a8db",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8ZIY799",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8ZIY799",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "c5822ed4-2047-4e64-acc6-d8cc15877b88",
                "userInfo": {
                    "email": "getse@vintagecellars.com",
                    "firstName": "Paola",
                    "lastName": "Noel",
                    "name": "Paola Noel",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "+16193724467",
                    "userId": "c5822ed4-2047-4e64-acc6-d8cc15877b88"
                },
                "userName": "Paola Noel",
                "uuid": "cabddc9e-1f4a-4a9a-8abf-32598e43a8db"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:02:21Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "4f65d3d3-be2d-4ce0-a91a-f6a06b793385",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "29|21800",
                "lockdownInfo": null,
                "message": "Keycard Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "00001110101010101001010001",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "keycard_entered_accepted",
                "userId": "2d34ed50-ac75-4c35-8804-5650db2dd276",
                "userInfo": {
                    "email": "chris@vintagecellars.com",
                    "firstName": "Christopher",
                    "lastName": "Noel",
                    "name": "Christopher Noel",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "+16193978965",
                    "userId": "2d34ed50-ac75-4c35-8804-5650db2dd276"
                },
                "userName": "Christopher Noel",
                "uuid": "4f65d3d3-be2d-4ce0-a91a-f6a06b793385"
            },
            "event_type": "DOOR_KEYCARD_ENTERED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-27T00:02:11Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "e1c148eb-93f4-4fb8-9cbb-ce74b5afb381",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9MPX218",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9MPX218",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "e1c148eb-93f4-4fb8-9cbb-ce74b5afb381"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:54:07Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "aa99dce1-9e21-4107-88f9-9f69400ecded",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9PUV859",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9PUV859",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "aa99dce1-9e21-4107-88f9-9f69400ecded"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:50:21Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "c649cddb-631a-44ef-9a55-fc0498a00332",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "9c17b638-4527-48e4-bcf0-57506a0adadd",
                "userInfo": {
                    "email": "Raquelitalugo@aol.com",
                    "firstName": "Raquelita",
                    "lastName": "Lugo",
                    "name": "Raquelita Lugo",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "9c17b638-4527-48e4-bcf0-57506a0adadd"
                },
                "userName": "Raquelita Lugo",
                "uuid": "c649cddb-631a-44ef-9a55-fc0498a00332"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:50:19Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "a23b2279-c47f-431a-baa1-bd1e49fe9d4d",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9JLM418",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9JLM418",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "953c179b-45f4-42bf-82a1-77b0739b4472",
                "userInfo": {
                    "email": "danielperry1956@gmail.com",
                    "firstName": "Daniel",
                    "lastName": "Perry",
                    "name": "Daniel Perry",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "953c179b-45f4-42bf-82a1-77b0739b4472"
                },
                "userName": "Daniel Perry",
                "uuid": "a23b2279-c47f-431a-baa1-bd1e49fe9d4d"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T23:49:47Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "514956f3-12ef-4df1-860d-a94a72c409f9",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9JLM",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9JLM",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "514956f3-12ef-4df1-860d-a94a72c409f9"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T23:49:37Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "74a6ff62-9894-4e51-aa74-4d9327183412",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9JLM418",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9JLM418",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "953c179b-45f4-42bf-82a1-77b0739b4472",
                "userInfo": {
                    "email": "danielperry1956@gmail.com",
                    "firstName": "Daniel",
                    "lastName": "Perry",
                    "name": "Daniel Perry",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "953c179b-45f4-42bf-82a1-77b0739b4472"
                },
                "userName": "Daniel Perry",
                "uuid": "74a6ff62-9894-4e51-aa74-4d9327183412"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T23:49:37Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "fcf6fb1f-b58e-4604-83ab-6badc12cd44e",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9DBH365",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9DBH365",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "3a725a22-5533-4394-9012-fa152d62e1b6",
                "userInfo": {
                    "email": "csquinteromd63@gmail.com",
                    "firstName": "Carolyn",
                    "lastName": "Quintero",
                    "name": "Carolyn Quintero",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "3a725a22-5533-4394-9012-fa152d62e1b6"
                },
                "userName": "Carolyn Quintero",
                "uuid": "fcf6fb1f-b58e-4604-83ab-6badc12cd44e"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T23:47:37Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "8a0d2ae2-503a-492f-88c5-7d4b512b1219",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "remote_unlock_accepted",
                "userId": "953c179b-45f4-42bf-82a1-77b0739b4472",
                "userInfo": {
                    "email": "danielperry1956@gmail.com",
                    "firstName": "Daniel",
                    "lastName": "Perry",
                    "name": "Daniel Perry",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "953c179b-45f4-42bf-82a1-77b0739b4472"
                },
                "userName": "Daniel Perry",
                "uuid": "8a0d2ae2-503a-492f-88c5-7d4b512b1219"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T23:47:28Z"
        },
        {
            "device_id": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "b135c043-2e39-4f1a-8e19-e16e57ea2f22",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "doorInfo": {
                    "accessControllerId": "d363e004-8422-4e89-9576-652cca93e896",
                    "accessControllerName": "Highland Gate",
                    "name": "Highland Gate"
                },
                "entityId": "4a0dcdbf-21bb-490b-96ce-1f5c3e21dcca",
                "entityName": "Highland Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "6524345eabba2bce5eb7650abe3b055a2b275300d05ec0b306cf8dc3a49a0d09",
                "lockdownInfo": null,
                "message": "BLE unlock attempt",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "6524345eabba2bce5eb7650abe3b055a2b275300d05ec0b306cf8dc3a49a0d09",
                "siteId": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
                "siteName": "Highland Gate",
                "type": "ble_unlock_attempt_accepted",
                "userId": "9be65bc0-6a06-47e4-856e-6686a273be4c",
                "userInfo": {
                    "email": "joe.zlotnicki@3zconsulting.com",
                    "firstName": "Joe",
                    "lastName": "Zlotnicki",
                    "name": "Joe Zlotnicki",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "9be65bc0-6a06-47e4-856e-6686a273be4c"
                },
                "userName": "Joe Zlotnicki",
                "uuid": "b135c043-2e39-4f1a-8e19-e16e57ea2f22"
            },
            "event_type": "DOOR_BLE_UNLOCK_ATTEMPT_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6b5e6bd5-5bca-4345-aec1-03525156d0cb",
            "timestamp": "2025-04-26T23:44:49Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "24cc46d2-1884-4011-b6b6-9c4a9dc02a92",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "DY61C38",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "DY61C38",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "24cc46d2-1884-4011-b6b6-9c4a9dc02a92"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:33:35Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "37d9bec7-84ab-43c0-8c44-dcb4662d44a8",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "DY61C38",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "DY61C38",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "37d9bec7-84ab-43c0-8c44-dcb4662d44a8"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:33:25Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "4ab02057-a092-48ae-bac4-fea18bd943a5",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "DY61C38",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "DY61C38",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "4ab02057-a092-48ae-bac4-fea18bd943a5"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:33:15Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "f30dc308-cf30-4db0-b239-cd1b24063578",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "DY61C38",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "DY61C38",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "f30dc308-cf30-4db0-b239-cd1b24063578"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:33:04Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "41942139-b8aa-4179-bfa4-e3b6a5179c81",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "DCE1983",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "DCE1983",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "6a674d9f-be89-49bb-9616-e01aecec60e9",
                "userInfo": {
                    "email": "sleepdoc2@me.com",
                    "firstName": "Rick",
                    "lastName": "Engel",
                    "name": "Rick Engel",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "6a674d9f-be89-49bb-9616-e01aecec60e9"
                },
                "userName": "Rick Engel",
                "uuid": "41942139-b8aa-4179-bfa4-e3b6a5179c81"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:22:08Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "732986ab-355f-47d4-bdaa-269f77fb6a72",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "33729X3",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "33729X3",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "447c7d28-9fbf-404c-8092-28951e293241",
                "userInfo": {
                    "email": "rc@listerconstruction.com",
                    "firstName": "Ron",
                    "lastName": "Lister",
                    "name": "Ron Lister",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "447c7d28-9fbf-404c-8092-28951e293241"
                },
                "userName": "Ron Lister",
                "uuid": "732986ab-355f-47d4-bdaa-269f77fb6a72"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T23:20:09Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "358e1fb9-f39a-42c6-b7e1-e8de24550b25",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7PBA083",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7PBA083",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "358e1fb9-f39a-42c6-b7e1-e8de24550b25"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:20:08Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "c2e2d648-3cf7-4a24-b89a-4f3055836491",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "19370478-47eb-44be-9cd3-4cbbffd8b483",
                "userInfo": {
                    "email": "stuoster39@gmail.com",
                    "firstName": "Stu",
                    "lastName": "Oster",
                    "name": "Stu Oster",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "+17604439879",
                    "userId": "19370478-47eb-44be-9cd3-4cbbffd8b483"
                },
                "userName": "Stu Oster",
                "uuid": "c2e2d648-3cf7-4a24-b89a-4f3055836491"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:19:58Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "ef43560b-ad8d-4c20-afd1-1a82cacc0e1d",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7PBA083",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7PBA083",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "ef43560b-ad8d-4c20-afd1-1a82cacc0e1d"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:19:57Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "4151023b-4511-4a3c-9ae0-2a4084c54e4d",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7PBA083",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7PBA083",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "4151023b-4511-4a3c-9ae0-2a4084c54e4d"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:19:47Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "6660febf-5780-4394-8306-f340d46c6c91",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7PBA083",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7PBA083",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "6660febf-5780-4394-8306-f340d46c6c91"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:19:36Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "02eb1046-8ede-490c-ab64-13e45fb35de7",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "26|57504",
                "lockdownInfo": null,
                "message": "Keycard Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "00001101011100000101000001",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "keycard_entered_accepted",
                "userId": "3cb526e3-e85b-46d6-bbef-3a6e5a46019b",
                "userInfo": {
                    "email": "colleen@listerconstruction.com",
                    "firstName": "Colleen",
                    "lastName": "Lister",
                    "name": "Colleen Lister",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "3cb526e3-e85b-46d6-bbef-3a6e5a46019b"
                },
                "userName": "Colleen Lister",
                "uuid": "02eb1046-8ede-490c-ab64-13e45fb35de7"
            },
            "event_type": "DOOR_KEYCARD_ENTERED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T23:19:30Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "0f46919a-cba2-4832-8e1c-46bdf4be3405",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "26|57504",
                "lockdownInfo": null,
                "message": "Keycard Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "00001101011100000101000001",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "keycard_entered_accepted",
                "userId": "3cb526e3-e85b-46d6-bbef-3a6e5a46019b",
                "userInfo": {
                    "email": "colleen@listerconstruction.com",
                    "firstName": "Colleen",
                    "lastName": "Lister",
                    "name": "Colleen Lister",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "3cb526e3-e85b-46d6-bbef-3a6e5a46019b"
                },
                "userName": "Colleen Lister",
                "uuid": "0f46919a-cba2-4832-8e1c-46bdf4be3405"
            },
            "event_type": "DOOR_KEYCARD_ENTERED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T23:19:27Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "b8aed957-adb9-44df-ae38-c5774bd39353",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7PBA083",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7PBA083",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "b8aed957-adb9-44df-ae38-c5774bd39353"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:19:25Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "4ae9c962-805a-484c-b8b7-8bac31122c64",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7PBA083",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7PBA083",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "4ae9c962-805a-484c-b8b7-8bac31122c64"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:19:15Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "7d864a7c-2963-4893-84b3-98c45f462dbd",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7PBA083",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7PBA083",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "7d864a7c-2963-4893-84b3-98c45f462dbd"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:19:05Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "6b922fdf-5e3e-418f-b9c8-d008c864e62f",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7PBA083",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7PBA083",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "6b922fdf-5e3e-418f-b9c8-d008c864e62f"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:18:54Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "51ba4b06-25d2-415c-b435-30a273838973",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7PBA083",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7PBA083",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "51ba4b06-25d2-415c-b435-30a273838973"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:18:44Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "9f025e76-ffc4-4745-921c-d0417d271b53",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "23336X1",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "23336X1",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "048041ff-9d15-4459-9e47-ef0fb935f4a4",
                "userInfo": {
                    "email": "spectrumplumbing@yahoo.com",
                    "firstName": "Dave",
                    "lastName": "Greaves",
                    "name": "Dave Greaves",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "048041ff-9d15-4459-9e47-ef0fb935f4a4"
                },
                "userName": "Dave Greaves",
                "uuid": "9f025e76-ffc4-4745-921c-d0417d271b53"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T23:11:59Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "c39a20ff-0403-42e9-8434-c071e848900e",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "26|58144",
                "lockdownInfo": null,
                "message": "Keycard Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "00001101011100011001000000",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "keycard_entered_accepted",
                "userId": "048041ff-9d15-4459-9e47-ef0fb935f4a4",
                "userInfo": {
                    "email": "spectrumplumbing@yahoo.com",
                    "firstName": "Dave",
                    "lastName": "Greaves",
                    "name": "Dave Greaves",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "048041ff-9d15-4459-9e47-ef0fb935f4a4"
                },
                "userName": "Dave Greaves",
                "uuid": "c39a20ff-0403-42e9-8434-c071e848900e"
            },
            "event_type": "DOOR_KEYCARD_ENTERED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T23:11:46Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "06ddb7ff-094b-43af-9d26-f05b0cb91f54",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8NEN012",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8NEN012",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "b1015b58-3ebc-442e-89a0-c250fb25b38e",
                "userInfo": {
                    "email": "jeffjohnsd@outlook.com",
                    "firstName": "Jeff",
                    "lastName": "Johnston",
                    "name": "Jeff Johnston",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "b1015b58-3ebc-442e-89a0-c250fb25b38e"
                },
                "userName": "Jeff Johnston",
                "uuid": "06ddb7ff-094b-43af-9d26-f05b0cb91f54"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:09:57Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "6ec4b7a1-7328-41de-87f0-ecc35a85b8de",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "6ec4b7a1-7328-41de-87f0-ecc35a85b8de"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:08:50Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "dfa68a28-ce43-4f90-80ad-0888a70b10dc",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "dfa68a28-ce43-4f90-80ad-0888a70b10dc"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:08:44Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "f51ffdb0-52a7-4b2a-97dd-80451f9c8adf",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "f51ffdb0-52a7-4b2a-97dd-80451f9c8adf"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:08:37Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "27904bb7-eb27-4c51-baf5-1c5472291691",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "27904bb7-eb27-4c51-baf5-1c5472291691"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:08:33Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "46f43063-70b8-49c4-a9b9-e055596d6377",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "46f43063-70b8-49c4-a9b9-e055596d6377"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:08:30Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "a2dc65e3-4556-463d-b8f8-7e5fa727b999",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "6RDZ772",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "6RDZ772",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "a2dc65e3-4556-463d-b8f8-7e5fa727b999"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:08:28Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "59781d71-b8da-4775-a05e-0d1defe206a0",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9KEH867",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9KEH867",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "44bab09e-8fa9-4161-892c-d6b2ce3a9fbf",
                "userInfo": {
                    "email": "garcia89@gmail.com",
                    "firstName": "Alex & Jaqueline",
                    "lastName": "Garcia",
                    "name": "Alex & Jaqueline Garcia",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "44bab09e-8fa9-4161-892c-d6b2ce3a9fbf"
                },
                "userName": "Alex & Jaqueline Garcia",
                "uuid": "59781d71-b8da-4775-a05e-0d1defe206a0"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T23:07:58Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "0158a1a6-dd47-46da-96be-39ae64813b64",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "17659H3",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "17659H3",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "3bdb3c3b-f6fe-4dc5-a307-1775e09489dd",
                "userInfo": {
                    "email": "sam@vantedgeplans.com",
                    "firstName": "Hussam",
                    "lastName": "Elfarra",
                    "name": "Hussam Elfarra",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "3bdb3c3b-f6fe-4dc5-a307-1775e09489dd"
                },
                "userName": "Hussam Elfarra",
                "uuid": "0158a1a6-dd47-46da-96be-39ae64813b64"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:59:37Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "02cee36c-0851-43f2-a16d-5f2ff36ad7d9",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "17659H3",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "17659H3",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "3bdb3c3b-f6fe-4dc5-a307-1775e09489dd",
                "userInfo": {
                    "email": "sam@vantedgeplans.com",
                    "firstName": "Hussam",
                    "lastName": "Elfarra",
                    "name": "Hussam Elfarra",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "3bdb3c3b-f6fe-4dc5-a307-1775e09489dd"
                },
                "userName": "Hussam Elfarra",
                "uuid": "02cee36c-0851-43f2-a16d-5f2ff36ad7d9"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:59:27Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "3f4faab3-b4e3-4aa0-8dae-f41126ee8ece",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "17659H",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "17659H",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "3f4faab3-b4e3-4aa0-8dae-f41126ee8ece"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:59:27Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "d961f1dd-fb0b-4a80-949f-04db681e1fa3",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "26|58147",
                "lockdownInfo": null,
                "message": "Keycard Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "00001101011100011001000110",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "keycard_entered_accepted",
                "userId": "3bdb3c3b-f6fe-4dc5-a307-1775e09489dd",
                "userInfo": {
                    "email": "sam@vantedgeplans.com",
                    "firstName": "Hussam",
                    "lastName": "Elfarra",
                    "name": "Hussam Elfarra",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "3bdb3c3b-f6fe-4dc5-a307-1775e09489dd"
                },
                "userName": "Hussam Elfarra",
                "uuid": "d961f1dd-fb0b-4a80-949f-04db681e1fa3"
            },
            "event_type": "DOOR_KEYCARD_ENTERED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:59:21Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "9fa28597-36f2-4242-86f0-682f48049423",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "48203K1",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "48203K1",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "52ebfee4-18e4-490d-be79-55e5aed25b94",
                "userInfo": {
                    "email": "1rickmills@gmail.com",
                    "firstName": "Rick",
                    "lastName": "Mills",
                    "name": "Rick Mills",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "52ebfee4-18e4-490d-be79-55e5aed25b94"
                },
                "userName": "Rick Mills",
                "uuid": "9fa28597-36f2-4242-86f0-682f48049423"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:59:18Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "9fe3bdad-6b47-4ce2-9e88-125769e9a431",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "48203K1",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "48203K1",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "52ebfee4-18e4-490d-be79-55e5aed25b94",
                "userInfo": {
                    "email": "1rickmills@gmail.com",
                    "firstName": "Rick",
                    "lastName": "Mills",
                    "name": "Rick Mills",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "52ebfee4-18e4-490d-be79-55e5aed25b94"
                },
                "userName": "Rick Mills",
                "uuid": "9fe3bdad-6b47-4ce2-9e88-125769e9a431"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:59:08Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "1de05736-4588-4eff-8d67-19d605dd0413",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "03K1",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "03K1",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "1de05736-4588-4eff-8d67-19d605dd0413"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:59:07Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "7ac31040-ad6a-45f3-90d0-59f6030a7760",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "203K1",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "203K1",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "7ac31040-ad6a-45f3-90d0-59f6030a7760"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:59:07Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "1f80693f-7a71-4910-b086-18f2d941e045",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8203K1",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8203K1",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "1f80693f-7a71-4910-b086-18f2d941e045"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:59:07Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "30033d09-bcb8-42f5-b36c-dcd862bd8b01",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7PVS569",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7PVS569",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "36e56cf1-f4bf-4a85-aee1-133e97879cff",
                "userInfo": {
                    "email": "jim.korinek@cbre.com",
                    "firstName": "Jim",
                    "lastName": "Korinek",
                    "name": "Jim Korinek",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "36e56cf1-f4bf-4a85-aee1-133e97879cff"
                },
                "userName": "Jim Korinek",
                "uuid": "30033d09-bcb8-42f5-b36c-dcd862bd8b01"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:58:06Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "1540ec4a-e4d0-4e3c-862f-a0f0f4b34dd5",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "26|57519",
                "lockdownInfo": null,
                "message": "Keycard Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "00001101011100000101011111",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "keycard_entered_accepted",
                "userId": "17bdfcdb-05ff-4387-97cf-4cc8e1dafe42",
                "userInfo": {
                    "email": "dawnkorinek@gmail.com",
                    "firstName": "Dawn",
                    "lastName": "Fuller",
                    "name": "Dawn Fuller",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "17bdfcdb-05ff-4387-97cf-4cc8e1dafe42"
                },
                "userName": "Dawn Fuller",
                "uuid": "1540ec4a-e4d0-4e3c-862f-a0f0f4b34dd5"
            },
            "event_type": "DOOR_KEYCARD_ENTERED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:57:59Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "c5f7eeef-e541-43a1-9e43-d7dcc9a5ae8f",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "48093A2",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "48093A2",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "15803619-63d3-4166-b1de-2fdd5b247516",
                "userInfo": {
                    "email": "beedaniel16@gmail.com",
                    "firstName": "Brook",
                    "lastName": "Daniel Husband",
                    "name": "Brook Daniel Husband",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "15803619-63d3-4166-b1de-2fdd5b247516"
                },
                "userName": "Brook Daniel Husband",
                "uuid": "c5f7eeef-e541-43a1-9e43-d7dcc9a5ae8f"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:55:17Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "5455df4c-83d4-4c63-a542-94f01b630749",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9DMR535",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9DMR535",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "1bcd95e7-5f5b-4519-80ee-0524114a8aa1",
                "userInfo": {
                    "email": "marie.kempka@gmail.com",
                    "firstName": "Marie",
                    "lastName": "Kempka",
                    "name": "Marie Kempka",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "1bcd95e7-5f5b-4519-80ee-0524114a8aa1"
                },
                "userName": "Marie Kempka",
                "uuid": "5455df4c-83d4-4c63-a542-94f01b630749"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:55:01Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "34f7ea1c-11b0-4bf2-b719-fa98c503d08a",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "DL991483",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "DL991483",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "34f7ea1c-11b0-4bf2-b719-fa98c503d08a"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:51:11Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "dbcc7744-9966-46cd-aba5-9a4c4d42b938",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "DLR91483",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "DLR91483",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "dbcc7744-9966-46cd-aba5-9a4c4d42b938"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:51:10Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "c69e292b-4b92-4017-a868-1b2c16dc8796",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "DLB91483",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "DLB91483",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "c69e292b-4b92-4017-a868-1b2c16dc8796"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:51:10Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "18f18b6f-71b5-42ff-837b-aee19eb7ef48",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "26|57545",
                "lockdownInfo": null,
                "message": "Keycard Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "00001101011100000110010011",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "keycard_entered_accepted",
                "userId": "e3088df6-23a0-40ac-9090-64dbeba06968",
                "userInfo": {
                    "email": "asiaweleski@mossy.com",
                    "firstName": "Anthony",
                    "lastName": "Siaweleski",
                    "name": "Anthony Siaweleski",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "e3088df6-23a0-40ac-9090-64dbeba06968"
                },
                "userName": "Anthony Siaweleski",
                "uuid": "18f18b6f-71b5-42ff-837b-aee19eb7ef48"
            },
            "event_type": "DOOR_KEYCARD_ENTERED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:51:06Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "7787b081-9b17-41f8-a652-19280eafd4fd",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "IRNFRE",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "IRNFRE",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "3eaac69f-d7a9-4c17-af2e-f6ac183e29fa",
                "userInfo": {
                    "email": "inspector@aboutcis.com",
                    "firstName": "Kent",
                    "lastName": "Schafer ",
                    "name": "Kent Schafer ",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "3eaac69f-d7a9-4c17-af2e-f6ac183e29fa"
                },
                "userName": "Kent Schafer ",
                "uuid": "7787b081-9b17-41f8-a652-19280eafd4fd"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:47:46Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "480e348b-dde9-4558-ba98-23fbdce97e79",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "IRNFRE",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "IRNFRE",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "3eaac69f-d7a9-4c17-af2e-f6ac183e29fa",
                "userInfo": {
                    "email": "inspector@aboutcis.com",
                    "firstName": "Kent",
                    "lastName": "Schafer ",
                    "name": "Kent Schafer ",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "3eaac69f-d7a9-4c17-af2e-f6ac183e29fa"
                },
                "userName": "Kent Schafer ",
                "uuid": "480e348b-dde9-4558-ba98-23fbdce97e79"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:47:36Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "e3230419-97bc-44bc-abad-e9abde3aab0b",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TMT085",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TMT085",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "4ff818ca-7d91-4fb5-9250-ae6e3804a841",
                "userInfo": {
                    "email": null,
                    "firstName": "Premteerth",
                    "lastName": "Sawh",
                    "name": "Premteerth Sawh",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "4ff818ca-7d91-4fb5-9250-ae6e3804a841"
                },
                "userName": "Premteerth Sawh",
                "uuid": "e3230419-97bc-44bc-abad-e9abde3aab0b"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:43:28Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "7e8edf38-e01a-4ac8-9bc5-d09de6d61bad",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "7TMT085",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "7TMT085",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "4ff818ca-7d91-4fb5-9250-ae6e3804a841",
                "userInfo": {
                    "email": null,
                    "firstName": "Premteerth",
                    "lastName": "Sawh",
                    "name": "Premteerth Sawh",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "4ff818ca-7d91-4fb5-9250-ae6e3804a841"
                },
                "userName": "Premteerth Sawh",
                "uuid": "7e8edf38-e01a-4ac8-9bc5-d09de6d61bad"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:43:18Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "2f2dae08-f328-4121-93dd-1b06db6c7683",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8VDV149",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8VDV149",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "2f2dae08-f328-4121-93dd-1b06db6c7683"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:39:45Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "a60904e2-b9b5-4048-a7f6-58db82dfd7fd",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8ULR121",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8ULR121",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "9dade04d-3f83-4f21-b44e-d10e56a3b336",
                "userInfo": {
                    "email": "ryryx69@gmail.com",
                    "firstName": "Richard",
                    "lastName": "Mallo",
                    "name": "Richard Mallo",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "9dade04d-3f83-4f21-b44e-d10e56a3b336"
                },
                "userName": "Richard Mallo",
                "uuid": "a60904e2-b9b5-4048-a7f6-58db82dfd7fd"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:29:16Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "22bb6fb9-79fd-4de0-bd80-fa0aff7a5850",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8SRW39",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8SRW39",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "22bb6fb9-79fd-4de0-bd80-fa0aff7a5850"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:24:29Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "b2554282-fed2-41e7-8b5c-f51a322d5478",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8SRW399",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8SRW399",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "lp_presented_accepted",
                "userId": "ea22fbba-569c-4bd4-8a18-0d1b8fccfe5a",
                "userInfo": {
                    "email": "alnajjarrawan@hotmail.com",
                    "firstName": "Rawan",
                    "lastName": "Alnajjar",
                    "name": "Rawan Alnajjar",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "ea22fbba-569c-4bd4-8a18-0d1b8fccfe5a"
                },
                "userName": "Rawan Alnajjar",
                "uuid": "b2554282-fed2-41e7-8b5c-f51a322d5478"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:24:29Z"
        },
        {
            "device_id": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "2ccf1efa-1cce-4152-a34d-a47aba338f04",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "doorInfo": {
                    "accessControllerId": "38c2c445-7c69-4d02-bb81-e444932db773",
                    "accessControllerName": "Main Gate",
                    "name": "Main Gate"
                },
                "entityId": "33c9b244-4f86-4e90-9f1b-19de59b50fa6",
                "entityName": "Main Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "26|58148",
                "lockdownInfo": null,
                "message": "Keycard Entered",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "00001101011100011001001001",
                "siteId": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
                "siteName": "Main Gate ",
                "type": "keycard_entered_accepted",
                "userId": "ea22fbba-569c-4bd4-8a18-0d1b8fccfe5a",
                "userInfo": {
                    "email": "alnajjarrawan@hotmail.com",
                    "firstName": "Rawan",
                    "lastName": "Alnajjar",
                    "name": "Rawan Alnajjar",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "ea22fbba-569c-4bd4-8a18-0d1b8fccfe5a"
                },
                "userName": "Rawan Alnajjar",
                "uuid": "2ccf1efa-1cce-4152-a34d-a47aba338f04"
            },
            "event_type": "DOOR_KEYCARD_ENTERED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "6057df87-b9a2-4231-b5fe-1657e89c89e6",
            "timestamp": "2025-04-26T22:24:18Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "2a882fd6-d312-4de6-bce7-7bb883cc9220",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "2b300b90-cbba-47ea-80ef-ca69a62d7bca",
                "userInfo": {
                    "email": "kathleendelmastro3@gmail.com",
                    "firstName": "Kathleen",
                    "lastName": "Delmastro",
                    "name": "Kathleen Delmastro",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "2b300b90-cbba-47ea-80ef-ca69a62d7bca"
                },
                "userName": "Kathleen Delmastro",
                "uuid": "2a882fd6-d312-4de6-bce7-7bb883cc9220"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:18:53Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "641730d0-2448-4408-aabb-f3e61f237c5a",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "5KDE529",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "5KDE529",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "641730d0-2448-4408-aabb-f3e61f237c5a"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:17:57Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "6229de65-69fe-4a9c-b914-347ab192bebe",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1",
                "userInfo": {
                    "email": "ryderzpaxton@gmail.com",
                    "firstName": "Ryder",
                    "lastName": "Paxton",
                    "name": "Ryder Paxton",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "595ed6c0-2ba5-4144-a8af-767a4844e3f1"
                },
                "userName": "Ryder Paxton",
                "uuid": "6229de65-69fe-4a9c-b914-347ab192bebe"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:17:38Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "2fd79c91-45ba-4931-9ab5-e8f743b0a5ba",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "8LIW249",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "8LIW249",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "2fd79c91-45ba-4931-9ab5-e8f743b0a5ba"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:17:33Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "70e83584-5931-4a57-9244-12d14886ed64",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9FRK076",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9FRK076",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_accepted",
                "userId": "6346bcc7-7cdc-40ae-8ecc-7281d403402a",
                "userInfo": {
                    "email": "spfurgie@gmail.com",
                    "firstName": "Scott",
                    "lastName": "Furgerson",
                    "name": "Scott Furgerson",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "6346bcc7-7cdc-40ae-8ecc-7281d403402a"
                },
                "userName": "Scott Furgerson",
                "uuid": "70e83584-5931-4a57-9244-12d14886ed64"
            },
            "event_type": "DOOR_LP_PRESENTED_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:15:49Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "a70686f8-2a6c-4eac-88df-551ddc15c060",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9MED309",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9MED309",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "a70686f8-2a6c-4eac-88df-551ddc15c060"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:14:53Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "17bfe8a7-ea18-4880-920e-c70044d77ce4",
            "event_info": {
                "accepted": true,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": null,
                "lockdownInfo": null,
                "message": "Remote Unlock via Mobile",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": null,
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "remote_unlock_accepted",
                "userId": "2b300b90-cbba-47ea-80ef-ca69a62d7bca",
                "userInfo": {
                    "email": "kathleendelmastro3@gmail.com",
                    "firstName": "Kathleen",
                    "lastName": "Delmastro",
                    "name": "Kathleen Delmastro",
                    "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                    "phone": "",
                    "userId": "2b300b90-cbba-47ea-80ef-ca69a62d7bca"
                },
                "userName": "Kathleen Delmastro",
                "uuid": "17bfe8a7-ea18-4880-920e-c70044d77ce4"
            },
            "event_type": "DOOR_REMOTE_UNLOCK_ACCEPTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:14:50Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "a10d4ed7-fc73-426e-a592-e4a2f6831986",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9MED309",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9MED309",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "a10d4ed7-fc73-426e-a592-e4a2f6831986"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:14:42Z"
        },
        {
            "device_id": "d0bd34d5-a8e6-49b8-8074-298418e56180",
            "device_type": "ACCESS_CONTROL",
            "end_timestamp": null,
            "event_id": "3614fd43-b9f6-4801-8fac-46b0241f7ba2",
            "event_info": {
                "accepted": false,
                "auxInputId": null,
                "auxInputName": null,
                "buildingId": "b61bed47-67fa-433e-9c90-494d1f470bb3",
                "buildingName": "Rimrock",
                "direction": null,
                "doorId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "doorInfo": {
                    "accessControllerId": "d00dd2ea-d0ed-44e7-b836-795e297867ad",
                    "accessControllerName": "Mesa Gate",
                    "name": "Mesa Gate"
                },
                "entityId": "d0bd34d5-a8e6-49b8-8074-298418e56180",
                "entityName": "Mesa Gate",
                "entityType": "door",
                "eventType": "user_action",
                "floorId": "eb3a4913-1919-4169-b431-39b305731b2b",
                "floorName": "1",
                "floors": null,
                "inputValue": "9MED309",
                "lockdownInfo": null,
                "message": "License Plate Presented",
                "organizationId": "5401889e-5a42-4a4f-b793-9d8db61d9342",
                "rawCard": "9MED309",
                "siteId": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
                "siteName": "Mesa Gate",
                "type": "lp_presented_rejected",
                "userId": null,
                "userInfo": null,
                "userName": null,
                "uuid": "3614fd43-b9f6-4801-8fac-46b0241f7ba2"
            },
            "event_type": "DOOR_LP_PRESENTED_REJECTED",
            "organization_id": "5401889e-5a42-4a4f-b793-9d8db61d9342",
            "site_id": "bf636a0b-e9f5-4e06-a7ff-a6f1c4c89f47",
            "timestamp": "2025-04-26T22:14:32Z"
        }
    ],
    "next_page_token": "1745705672"
}
2025-04-26 22:15:29,692 - __main__ - INFO - Successfully retrieved 200 access events.
2025-04-26 22:15:29,693 - src_helix.api_utils - INFO - Generated JSON template: src_helix/api-json/test_access_events_api.json
PASS: Access Events

--------------------------------------------------------------------------------
Tests Skipped by Design:
--------------------------------------------------------------------------------
SKIP: LPR Timestamps (Plate/Cam) (test_lpr_timestamps_api.py)

================================================================================
 Test Summary
================================================================================
 Total Tests Defined: 12
 Tests Attempted: 11
 Passed: 11
 Failed: 0
 Skipped: 1
================================================================================
