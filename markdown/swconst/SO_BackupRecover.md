---
title: "System Options > Backup/Recover"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_BackupRecover.htm"
---

# System Options > Backup/Recover

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture corresponds to the settings on that dialog.
- titled

  [Obsolete
  Enumerators](#Obsolete)

  contains enumerators that previously appeared on the

  dialog
  but are now obsolete.

(Table)=========================================================

| Setting | Get/Set Methods | Return value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Auto-recover - Save auto-recover info every | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoSaveEnable) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swAutoSaveEnable,
< OnFlag >) | Boolean value | Specifies whether auto-recovery is enabled |
| Auto-recover - Save auto-recover info every - < n > | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAutoSaveInterval) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAutoSaveInterval,
< Value >) | Integer value: 0 = Turn off auto-recovery non-0 = number of operations between auto-recoveries,
up to 120 |  |
| Auto-recover - Save auto-recover info every - < units > | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAutoSaveIntervalMode) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swAutoSaveIntervalMode,
swAutoSaveIntervalMode_e.< Value >) | See swAutoSaveIntervalMode_e for valid options | Specifies auto-recover mode |
| Auto-recover - Auto-recover folder | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swAutoSaveDirectory) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swAutoSaveDirectory,
< Value >) | String value |  |
| Backup - Number of backup copies per document (Not supported in SOLIDWORKS
Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swBackupEnable) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swBackupEnable,
< OnFlag >) | Boolean value | Specifies whether backup copies of the document are created before any
changes to the document are made |
| Backup - Number of backup copies per document - < n > (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBackupCopiesPerDocument) ISldWorks::SetUserPreferInteger StringValue_e.swBackupCopiesPerDocument,
< Value >) | Integer value: 1 - 10 | Specifies number of backup copies per document |
| Backup - Backup folder Backup - Save backup files in the same location as the original (Not
supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSaveBackupFilesInSameLocationAsOriginal) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSaveBackupFilesInSameLocationAsOriginal,
< OnFlag >) | Boolean value: True: Specifies to save backup files in same location
as original file False: Specifies to save backup files in the folder
specified in Backup folder |  |
| Backup - Backup folder - < folder > (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swBackupDirectory) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swBackupDirectory,
< Value >) | String value | Specifies the folder
where to save backup files |
| Backup - Remove backups older (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swBackupRemoveEnable) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swBackupRemoveEnable,
< OnFlag >) | Boolean value | Specifies whether backup
documents older than the specified days are removed when you start up
SOLIDWORKS |
| Backup - Remove backups older than < n >
days (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBackupRemoveInterval) ISldWorks::SetUserPreferenceIntegerValue (swUserPreferenceIntegerValue_e.swBackupRemoveInterval,
< Value >) | Integer value: 1 - 30 | Specifies the number of days when to remove backup copies of a document |

Obsolete Enumerators

(Table)=========================================================

| Enumerator | Comment |
| --- | --- |
| swBackupAfterMeshOrRunSimulationStudy | Obsolete |
