# Alerts LP and Video 
- today: sends via email only to administrators for LP of interest.

- goal is to send the alert for license plates of interest, but not the video, to one email associated with each LP
- Verkada db allows
- designate LP of interest
- every user has an email address
- carrie wants to associate an email with each LP of interest - does Verkada support that?

- read about Helix events
- https://www.verkada.com/helix/


API Info
---
LPR Webhook Object provides LPR events with LP numbers, but does not appear to provide LP of interest.
Sample Notification Webhook Object

JSON

{
  "org_id": "8b0f904a-998c-4cef-a664-630846dfc68e",
  "webhook_type": "lpr",
  "created_at": 1742259179,
  "webhook_id": "afa8082c-2cd6-431d-b0f8-e9ea3c5aa563",
  "data": {
    "camera_id": "b018c3c4-f1e9-424e-b911-c09c5fdab0b7",
    "created": 1742259177,
    "detected": 1742259179426,
    "license_plate_number": "ABC123",
    "confidence": 0.9558042857142857,
    "crop": [
      0.9553524851799011,
      0.991522490978241,
      0.11374980956315994,
      0.15500019490718842
    ],
    "image_url": "IMAGE_URL"
  }
}

Looking at online alerts every LPoI includes a PoI.  The PoI field could be used for email addresses.

---

You can create a Helix Event Type through APIs.
- but not known if it is useful at this point
- I think this is to send events to verkada that they can attach to certain events

---
Get Alerts
get https://{region}.verkada.com/cameras/v1/alerts
Returns alerts for an organization within a specified time range.

This API allows selecting alerts, including LP of interest alerts (I think) for a time period.
- don't yet know if the webhook event would have the LP of interest field
- however, this API could be used for a polling implementation. Every NN minutes.
- note that Person (LP?) of interest alerts include a label. Could this label be the email address?

Alert types include camera offline, camera online, tamper, motion, crowd, and Person of Interest alerts.
Person of Interest alerts include the label set for the person.

---

Another API
Get seen license plates
get https://{region}.verkada.com/cameras/v1/analytics/lpr/images
Returns the timestamps, detected license plate numbers, and images of all license plates seen by a camera.

---

Get All License Plates of Interest
get https://{region}.verkada.com/cameras/v1/analytics/lpr/license_plate_of_interest
Returns creation time, description, and license plate number for all License Plates of Interest for an organization.
Could use this one to poll for LP of interest. Refresh every NN minutes.
- perhaps description field could be used for email address
- then with this list could correlate with LPR events.
- but if you already have to use the helix api and poll for LP of interested, then get events too?


Questions for tech
1. Do the webhook event records note LP of interest and their description field?
2. Would it make sense to use Get Alerts in conjunction with Get LPoI?