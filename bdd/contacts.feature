Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <name>, <last>
  When add new contact to the list
  Then the new contact list is equal to the old list with new contact

  Examples:
  | name | last |
  | Hokage | Naruto |
  | Shukaku | Kuby |


Scenario Outline: Modify contact
  Given a non-empty contact list
  Given a random contact from list
  When modify the chosen contact with a new values <name>, <last>
  Then the new contact list is equal to the old list with modified contact

  Examples:
  | name | last |
  | Sakur1a | Ken1zi |
  | Hinat1a | Uzuma1ki |

Scenario: Delete contact
  Given a non-empty contact list
  Given a random contact from list
  When delete the random contact
  Then the new contact list is equal to the old list without deleted contact
