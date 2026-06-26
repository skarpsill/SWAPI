---
title: "Compare Geometry Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Compare_Geometry_VBNET.htm"
---

# Compare Geometry Example (VB.NET)

This example shows how to use the SOLIDWORKS Utilities API to compare
geometries in two part documents.

```
'---------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities interop assembly as a reference
'    (right-click the project in Project Explorer, click Add Reference >
'     browse to install_dir\api\redist > SolidWorks.Interop.gtswutilities.dll).
' 3. Verify that the specified files exist.
' 4. Verify that C:\test\ exists.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Creates C:\test\Report\gtReportIndex.htm.
' 2. Gets the face and volume comparison statuses.
' 3. Examine the Immediate window, graphics area, and
'    C:\test\report\gtReportIndex.htm.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'--------------------------------------------------------------------------------
```

Imports SOLIDWORKS.Interop.sldworks

Imports SOLIDWORKS.Interop.swconst

Imports SOLIDWORKS.Interop.gtswutilities

Imports System

Imports System.Diagnostics

Partial Class SOLIDWORKSMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swUtil As gtcocswUtilities

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swUtilCompGeom As gtcocswCompareGeometry

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
longStatus As gtError_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bAddToBinder As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bOverwrite As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
errorCode As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the SOLIDWORKS Utilities tool interface

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUtil
= swapp.**GetAddInObject**("Utilities.UtilitiesApp")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the CompareGeometry tool

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUtilCompGeom
= swUtil.GetToolInterface(2, errorCode)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not errorCode = gtError_e.gtNOErr Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Error
getting compare geometry tool.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

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
volDiffStatus As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
faceDiffStatus As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file1
= "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file2
= "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_b.sldprt"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longStatus
= swUtilCompGeom.CompareGeometry3(file1,
"", file2, "", gtGdfOperationOption_e.gtGdfFaceAndVolumeCompare,
gtResultOptions_e.gtResultSaveReport, "C:\test\Report", bAddToBinder,
bOverwrite, volDiffStatus, faceDiffStatus)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not longStatus = gtError_e.gtNOErr Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Error
comparing geometries.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
diffStatus("Volume comparison", volDiffStatus)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
diffStatus("Face comparison", faceDiffStatus)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Perform any necessary clean up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longStatus
= swUtilCompGeom.Close()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
diffStatus(ByVal name As String, ByVal diffCode As gtVolDiffStatusOptionType_e)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(name)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Select
Case diffCode

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtVolDiffStatusOptionType_e.gtSuccess

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Succeeded")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtVolDiffStatusOptionType_e.gtNotPerformed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Not
performed")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtVolDiffStatusOptionType_e.gtCanceled

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Canceled")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtVolDiffStatusOptionType_e.gtFailed

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Failed")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtVolDiffStatusOptionType_e.gtIdenticalParts

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Identical
parts")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtVolDiffStatusOptionType_e.gtDifferentParts

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Different
parts")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtVolDiffStatusOptionType_e.gtNoSolidBody

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("No
solid body found")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
gtVolDiffStatusOptionType_e.gtAlreadySaved

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Already
saved")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Select

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class
