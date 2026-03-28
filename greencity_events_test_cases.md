# Test Cases: GreenCity — Events Page
**URL:** https://www.greencity.cx.ua/#/greenCity/events

---

## TC-01: Display of Events List on the Events Page

**Preconditions:**
- The user is on the GreenCity website.
- The Events page is accessible at `https://www.greencity.cx.ua/#/greenCity/events`.

| Step | Action | Data | Expected Result |
|------|--------|------|-----------------|
| 1. | Open the browser and navigate to the Events page | `https://www.greencity.cx.ua/#/greenCity/events` | The Events page is loaded successfully without errors. |
| 2. | Observe the page content | — | A list of available events is displayed on the page. |
| 3. | Check each event card | — | Each event card contains: title, date, location, and event image. |

---



## TC-02: Join an Event as an Authorized User

**Preconditions:**
- The user is registered and logged in to GreenCity.
- The user is on the Event Details page of an open event.
- The event has available seats.

| Step | Action | Data | Expected Result |
|------|--------|------|-----------------|
| 1. | Navigate to the Event Details page | — | The "Join event" button is visible. |
| 2. | Click the "Join event" button | — | A confirmation dialog or success notification appears. |
| 3. | Verify the button state after joining | — | The "Join event" button is replaced by the "Cancel request" button. |
| 4. | Refresh the page | — | The "Cancel request" button is still displayed (state is persisted). |

---

## TC-03: Cancel Event Participation

**Preconditions:**
- The user is registered and logged in to GreenCity.
- The user has previously joined an event.
- The user is on the Event Details page.

| Step | Action | Data | Expected Result |
|------|--------|------|-----------------|
| 1. | Navigate to the Event Details page where the user is already a participant | — | The "Cancel request" button is visible. |
| 2. | Click the "Cancel request" button | — | A confirmation pop-up or notification appears asking to confirm cancellation. |
| 3. | Confirm the cancellation | — | A success notification is displayed: "Your request has been cancelled." |
| 4. | Verify the button state | — | The "Cancel request" button is replaced by the "Join event" button. |

---

## TC-04: Attempt to Join an Event as an Unauthorized User

**Preconditions:**
- The user is NOT logged in.
- The user is on the Events page.

| Step | Action | Data | Expected Result |
|------|--------|------|-----------------|
| 1. | Open the Events page | `https://www.greencity.cx.ua/#/greenCity/events` | The Events page loads with a list of available events. |
| 2. | Click on any event card | — | The user is redirected to the Event Details page. |
| 3. | Click the "Join event" button | — | The user is redirected to the Login page or a pop-up appears prompting to sign in. |
| 4. | Verify that the user is NOT added to the event | — | No participation record is created for the event. |

---



## TC-05: Page Load Performance on Events Page

**Preconditions:**
- The user has a stable internet connection.
- The browser cache is cleared.

| Step | Action | Data | Expected Result |
|------|--------|------|-----------------|
| 1. | Open a new browser tab | — | Browser is ready. |
| 2. | Navigate to the Events page | `https://www.greencity.cx.ua/#/greenCity/events` | The page starts loading. |
| 3. | Measure page load time using DevTools (Network tab) | — | The page fully loads within **3 seconds**. |
| 4. | Verify that all event images are loaded | — | All event card images are displayed without broken icons or placeholders. |
