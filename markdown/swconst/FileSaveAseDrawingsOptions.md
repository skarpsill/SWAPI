---
title: "System Options > Export > EDRW/EPRT/EASM"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileSaveAseDrawingsOptions.htm"
---

# System Options > Export > EDRW/EPRT/EASM

This topic contains two tables. The information in the table:

- appearing immediately after the screen capture corresponds
  to the settings on that dialog.
- titled

  [Obsolete
  Enumerators](#Obsolete)

  contains enumerators that previously appeared on the
  dialog but are now obsolete.

To display the dialog:

Click**Tools > Options > System Options > Export > EDRW/EPRT/EASM**in**File Format**.

- or -

1. Click

  File > Save As

  .
2. In

  Save as type

  , select

  eDrawings

  .
3. Click

  Options

  .

Exporting in the EDRW/EPRT/EASM file format is not supported in SOLIDWORKS
Connected.

(Table)=========================================================

| Setting | Get/Set Methods | Return Value or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Enable Measure (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsOkayToMeasure) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsOkayToMeasure,
< OnFlag >) | Boolean value | Specifies whether to enable measurement of geometry in eDrawings file |
| Allow STL export (Not supported in SOLIDWORKS
Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsExportSTLOkay) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsExportSTLOkay,
< OnFlag >) | Boolean value | Specifies whether to allow recipients of eDrawings file to save it as
STL file from eDrawings Viewer |
| Save table features (Not supported in SOLIDWORKS
Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsSaveBOM) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsSaveBOM,
< OnFlag >) | Boolean value |  |
| Save file properties (Not supported in SOLIDWORKS
Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSaveFileProperties) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSaveFileProperties,
< OnFlag >) | Boolean value |  |
| Save file properties for each component in the assembly (Not supported in SOLIDWORKS
Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSaveFilePropertiesForEachComp) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSaveFilePropertiesForEachComp,
< OnFlag >) | Boolean value | For SOLIDWORKS assemblies only; valid only if Save file properties is set to
true |
| Drawings - Save shaded data (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsSaveShadedDataInDrawings) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsSaveShadedDataInDrawings,
< OnFlag >) | Boolean value | For SOLIDWORKS drawings only; specifies whether to save shaded data
from SOLIDWORKS drawing document in published eDrawings file |
| Drawings -
Include layers set to not print (Not supported in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsIncludeLayersNotToPrint) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsIncludeLayersNotToPrint,
< OnFlag >) | Boolean value | Specifies whether to include layers set not to print |
| Motion Studies - Save Motion Studies (Not supported in SOLIDWORKS
Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsSaveAnimationOkay) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsSaveAnimationOkay,
< OnFlag >) | Boolean value | Specifies whether to save motion studies to eDrawings file |
| Save each motion study in every configuration - or - Save only in last configuration (Not supported in SOLIDWORKS
Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsSaveAnimationToAllConfigs) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsSaveAnimationToAllConfigs,
< OnFlag >) | Boolean value: True: Save each motion study in every configuration False: save each motion study only in the configuration
in which it was last calculated | Specifies how to save motion studies to eDrawings files |
| Recalculate the motion study if the results are out of date (Not supported
in SOLIDWORKS Connected) | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsSaveAnimationRecalculate) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEDrawingsSaveAnimationRecalculate,
< OnFlag >) | Boolean value | Specifies whether to recalculate the motion study or use existing results
in eDrawings file; valid only if swEDrawingsSaveAnimationToAllConfigs is set to
False |

Obsolete Enumerators

(Table)=========================================================

| Enumerator | Comment |
| --- | --- |
| swEDrawingsCompression | Obsolete |
| swEdrawingsSaveAsSelectionOption | Obsolete |
| swEmodelSelectionList | Obsolete |
