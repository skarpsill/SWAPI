---
title: "Compare Geometry Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Compare_Geometry_CSharp.htm"
---

# Compare Geometry Example (C#)

This example shows how to use the SOLIDWORKS Utilities API to compare
geometries in two part documents.

```
'---------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities interop assembly as a reference
'    (right-click the project in Project Explorer, click Add Reference >
'     browse to install_dir\api\redist > Solidworks.Interop.gtswutilities.dll).
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

using SOLIDWORKS.Interop.sldworks;

using SOLIDWORKS.Interop.swconst;

using SOLIDWORKS.Interop.gtswutilities;

using System;

using System.Diagnostics;

namespace CompareGeometry_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SOLIDWORKSMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}gtcocswUtilities
swUtil = default(gtcocswUtilities);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}gtcocswCompareGeometry
swUtilCompGeom = default(gtcocswCompareGeometry);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}gtError_e
longStatus = default(gtError_e);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bool
bAddToBinder = false;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bool
bOverwrite = false;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
errorCode = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the SOLIDWORKS Utilities tool interface

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUtil
= (gtcocswUtilities)swApp.**GetAddInObject**("Utilities.UtilitiesApp");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Get the CompareGeometry tool

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUtilCompGeom
= (gtcocswCompareGeometry)swUtil.GetToolInterface(2,
out errorCode);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(!(errorCode == (int)gtError_e.gtNOErr))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Error
getting compare geometry tool.");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Compare the volumes and faces of the specified part documents

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Save the results to a file in the specified path

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bAddToBinder
= false;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bOverwrite
= true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
file1 = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
file2 = null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
volDiffStatus = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
faceDiffStatus = 0;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file1
= "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\swutilities\\bracket_a.sldprt";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file2
= "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\swutilities\\bracket_b.sldprt";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longStatus
= (gtError_e)swUtilCompGeom.CompareGeometry3(file1,
"", file2, "", (int)gtGdfOperationOption_e.gtGdfFaceAndVolumeCompare,
(int)gtResultOptions_e.gtResultSaveReport, "C:\\test\\Report",
bAddToBinder, bOverwrite, ref volDiffStatus,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ref
faceDiffStatus);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(!(longStatus == gtError_e.gtNOErr))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Error
comparing geometries.");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}diffStatus("Volume
comparison", volDiffStatus);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}diffStatus("Face
comparison", faceDiffStatus);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//
Perform any necessary clean up

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}longStatus
= (gtError_e)swUtilCompGeom.Close();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void diffStatus(string name, int diffCode)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(name);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}switch
(diffCode)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtSuccess:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Succeeded");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtNotPerformed:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Not
performed");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtCanceled:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Canceled");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtFailed:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Failed");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtIdenticalParts:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Identical
parts");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtDifferentParts:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Different
parts");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtNoSolidBody:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("No
solid body found");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}case
(int)gtVolDiffStatusOptionType_e.gtAlreadySaved:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Already
saved");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}break;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("
");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
