---
title: "SldWorks::LoadFile2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SldWorks/SldWorks__LoadFile2.htm"
---

# SldWorks::LoadFile2

This method is obsolete and has been superseded
by[SldWorks::LoadFile3](SldWorks__LoadFile3.htm).

Description

This method loads a non-native SolidWorks file
(for example, *.kadov_tag{{<ignored>}}igskadov_tag{{</ignored>}},
*.kadov_tag{{<ignored>}}dxfkadov_tag{{</ignored>}}, and
so on).

Syntax (OLE Automation)

retval = SldWorks.LoadFile2 (kadov_tag{{<ignored>}}FileNamekadov_tag{{</ignored>}},kadov_tag{{<ignored>}}ArgStringkadov_tag{{</ignored>}})

(Table)=========================================================

| Input: | ( BSTR ) FileName | Full path and filename of the non-native SolidWorks file to import |
| --- | --- | --- |
| Input: | ( BSTR ) ArgString | Space-separated string that allows optional arguments to be specified
when opening a foreign file (see Remarks ) |
| Return: | ( VARIANT_BOOL )
retval | TRUE if the file type is understood, FALSE if the file type is not known NOTE : This return value does
not indicate that the file import is successful; instead, it means that
the filename extension is recognized |

Syntax (kadov_tag{{<ignored>}}COMkadov_tag{{</ignored>}})

status = SldWorks->LoadFile2 ( FileName, ArgString,
&retval )

(Table)=========================================================

| Input: | (BSTR) FileName | Full path and filename of the non-native SolidWorks file to import |
| --- | --- | --- |
| Input: | (BSTR) ArgString | Space-separated string that allows optional arguments to be specified
when opening a foreign file (see Remarks ) |
| Output: | (VARIANT_BOOL) retval | TRUE if the file type is understood, FALSE if the file type is not known NOTE : This return value does
not indicate that the file import is successful; instead, it means that
the filename extension is recognized |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The general form of ArgString is BOOLEAN and enumerator
arguments, which should be passed as a string.

(Table)=========================================================

| If importing a... | Then set ArgString to... |
| --- | --- |
| DXF/DWG file | a space-separated list: < PaperSize > specifies
the sheet size: -1 = Translator attempts to figure out the sheet size using the foreign file;
this is the default if you do not specify any values 0 =
A (Horizontal) 1 = A (Vertical) 2 = B 3 = C 4 = D 5 = E 6 = A4 7 = A4 (Vertical) 8 = A3 9 = A2 10 = A1 11 = A0 < LengthUnit > specifies the default
length units : -1 = Translator attempts to figure out the default length unit using the
foreign file; this is the default if you do not specify any values 0 =
MM 1 = CM 2 = METER 3 = INCHES 4 = FEET 5 = FEETINCHES < MoveEntities > =
Not used. Specify 0, if necessary. < ImportToSheetFormat > 0 = Import entities to the drawing sheet; this is the default value if you
do not specify a value 1 = Import entities to the sheet format Examples To import a DXF/DWG file named Draw1.DXF with a sheet size of A3 and default length units in millimeters: swApp.LoadFile2 "C:\temp\Draw1.DXF",
"8 0" To only specify to use default length units in millimeters in < LengthUnit >, you must also specify
-1 for < PaperSize >: swApp.LoadFile2 "C:\temp\Draw1.DXF", "-1
0" To only specify to import to the sheet format in < ImportToSheetFormat >, you must also
specify -1 for both < PaperSize >
and < LengthUnit >, and 0 for < MoveEntities >: swApp.LoadFile2 "C:\temp\Draw1.DXF", "-1
-1 0 1" |
| Pro/E file | To
import features, use R To
import geometry, use: B – Direct
geometry import with knitting C – Direct
geometry import without knitting D – Geometry
import with knitting E – Geometry
import without knitting S – Surface
geometry import with knitting These arguments are case sensitive. Specifying one of these options
suppresses dialog. |
| Non DXF/DWG and Pro/E files | To
import the foreign file into a new SolidWorks document, use r To
insert the foreign file into an existing SolidWorks part document, use i For example, to import an IGES file named measuring_cup.igs into a new SolidWorks document: swApp.LoadFile2 "D:\Samples\measuring_cup.IGS",
"r" NOTES: Whether
or not the result is a surface or solid depends on the import options.
See Import and Export File Options for details. If
ArgString is set to an empty string , then dialogs may be presented to the end-user during translation. |

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks_Object$$**$$ZFileOperations$$**$$ZImportExportFiles$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SldWorks\SldWorks__LoadFile2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXImportedFileImportedFeature$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\SldWorks\SldWorks__LoadFile2.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
