---
title: "Compare Geometry (VBA)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swutilitiesapi/Compare_Geometry_VB6.htm"
---

# Compare Geometry (VBA)

## Compare Geometry Example (VBA)

This example shows how to use the SOLIDWORKS Utilities API to compare
geometries in two part documents.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities type library as a reference
'    (in the SOLIDWORKS Microsoft Visual Basic for Applications IDE, click
'    Tools > References > SolidWorks Utilities <version> Type Library).
' 3. Verify that the specified parts exist.
' 4. Verify that C:\test\ exists.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Creates the geometry comparison report, C:\test\Report\gtReportIndex.htm.
' 2. Gets face and volume comparison statuses.
' 3. Examine the Immediate window, graphics area, and
'    and C:\test\Report\gtReportIndex.htm.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'------------------------------------------------------------------------------
```

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swappkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swUtilkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SWUtilities.gtcocswUtilities

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swUtilCompGeomkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SWUtilities.gtcocswCompareGeometry

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
longStatuskadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
gtError_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bAddToBinderkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bOverwritekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Connect to SOLIDWORKS

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swapp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the SOLIDWORKS Utilities tool interface

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swUtil = swapp.**GetAddInObject**("Utilities.UtilitiesApp")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the CompareGeometry tool

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swUtilCompGeom = swUtil.**GetToolInterface**(2, longStatus)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not longStatus = gtNOErr Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Error getting compare geometry tool."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Compare the volumes and faces of the specified part documents

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bAddToBinder
= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bOverwrite
= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
file1 As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
file2 As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
volDiffStatus As gtVolDiffStatusOptionType_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
faceDiffStatus As gtVolDiffStatusOptionType_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file1
= "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file2
= "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_b.sldprt"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longStatus
= swUtilCompGeom.CompareGeometry3(file1,
"", file2, "", gtGdfFaceAndVolumeCompare, gtResultSaveReport,
"C:\test\Report", bAddToBinder, bOverwrite, volDiffStatus, faceDiffStatus)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not longStatus = gtNOErr Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Error comparing geometries."

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
diffStatus("Volume comparison", volDiffStatus)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
diffStatus("Face comparison", faceDiffStatus)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Perform any necessary clean up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longStatus
= swUtilCompGeom.**Close**()

End Sub

Sub diffStatus(ByVal name As String, ByVal diffCode As
gtVolDiffStatusOptionType_e)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Select
Case diffCode

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtSuccess

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Succeeded"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtNotPerformed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Not performed"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtCanceled

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Canceled"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtFailed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Failed"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtIdenticalParts

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Identical parts"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtDifferentParts

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Different parts"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtNoSolidBody

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"No solid body found"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtAlreadySaved

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Already saved"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Select

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

End Sub
