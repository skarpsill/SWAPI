---
title: "Set Tolerances and Compare Geometry Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Set_Tolerances_and_Compare_Geometry_VBNET.htm"
---

# Set Tolerances and Compare Geometry Example (VB.NET)

This example shows how to set the tolerances and then
compare the volume and geometry of two versions of the same part using the SOLIDWORKS Utilities API.

'------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(in
SOLIDWORKS, clickTools > Add-Ins
> SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities interop assembly as
a reference
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(right-click
the project in Project Explorer, click**Add Reference >**
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}browse
toinstall_dir\api\redist>SolidWorks.Interop.gtswutilities.dll).
' 3. Verify that the specified files exist.
' 4. Verify thatC:\test\exists.
'
' Postconditions:
' 1. Creates a geometry comparison report,C:\test\Report\gtReportIndex.htm.
' 2. Gets position and angular tolerance statuses.
' 3. Gets face and volume comparison statuses.
' 4. Examine the Immediate window, graphics area, andC:\test\Report\gtReportIndex.htm.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'-------------------------------------------------------------------------

Imports SOLIDWORKS.Interop.sldworks

Imports SOLIDWORKS.Interop.swconst

Imports SOLIDWORKS.Interop.gtswutilities

Imports System

Imports System.Diagnostics

Imports System.Runtime.InteropServices

Partial Class SOLIDWORKSMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Part As PartDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part
= swApp.**ActiveDoc**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swUtil As gtcocswUtilities

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swUtilCompGeom As gtcocswCompareGeometry

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
OUtils As gtcocswUtilOptions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
file1 As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
file2 As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
reportname As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
errorcode As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
posTol As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
angTol As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
AddToDesignBinder As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
OverwriteReport As Boolean

kadov_tag{{<spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}reportname
= "C:\test\Report"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddToDesignBinder
= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OverwriteReport
= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get pointer to SOLIDWORKS Utilities interface

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUtil
= swApp.**GetAddInObject**("Utilities.UtilitiesApp**"**)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get pointer to SOLIDWORKS Utilities Compare Geometry tool

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUtilCompGeom
= swUtil.GetToolInterface(gtSwTools_e.gtSwToolGeomDiff,
errorcode)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get SOLIDWORKS Utilities options

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}OUtils
= swUtil.Options

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}posTol
= 0.0001 ' Meters

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}angTol
= 0.000001 ' Radians

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set position tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}errorcode
= OUtils.SetPositionTolerance(posTol)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Position
tolerance is set." & " gtError_e: " & errorcode)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set angular tolerance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}errorcode
= OUtils.SetAngularTolerance(angTol)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Angular
tolerance is set." & " gtError_e: " & errorcode)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
volDiffStatus As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
faceDiffStatus As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file1
= "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file2
= "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_b.sldprt"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Compare the geometry of the faces and volumes and save results to a report

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}errorcode
= swUtilCompGeom.CompareGeometry3(file1,
"", file2, "", gtGdfOperationOption_e.gtGdfFaceAndVolumeCompare,
gtResultOptions_e.gtResultSaveReport, reportname, AddToDesignBinder, OverwriteReport,
volDiffStatus, faceDiffStatus)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not errorcode = gtError_e.gtNOErr Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Error
comparing geometries. Inspect gtError_e = " & errorcode &
" in the API help.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
diffStatus("Volume comparison", volDiffStatus)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Call
diffStatus("Face comparison", faceDiffStatus)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Perform any necessary cleanup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}errorcode
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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class
