---
title: "Modeler::CreateBodiesFromSheets"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__CreateBodiesFromSheets.htm"
---

# Modeler::CreateBodiesFromSheets

This method is obsolete and has been superseded
by[Modeler::CreateBodiesFromSheets2](sldworksAPI.chm::/Modeler/Modeler__CreateBodiesFromSheets2.htm).

Description

This method sews sheets to
make a sheet body or solid body.

Syntax (OLE Automation)

results = Modeler.CreateBodiesFromSheets ( sheets,
options, error)

(Table)=========================================================

| Input: | (VARIANT) sheets | VARIANT of type SafeArray containing
the sheets |
| --- | --- | --- |
| Input: | (long) options | Type of body to create as defined
by swSheetSewingOption_e |
| Property: | (long) error | Error as defined by swSheetSewingError_e |
| Output: | (VARIANT) results | VARIANT of type SafeArray of
the results |

Syntax (COM)

status = Modeler->ICreateBodiesFromSheets ( nSheets,
sheets, options, nResults, results, &error)

Parameters Table Start

(Table)=========================================================

| Input: | (long) nSheets | Number of sheets |
| --- | --- | --- |
| Input: | (LPUNKNOWN) sheets | Pointer to the sheets |
| Input: | (long) options | Type of body to create as defined
by swSheetSewingOption_e |
| Property: | (long) nResults | Number of results |
| Property: | (LPUNKNOWN) results | Pointer to the results |
| Output: | (long) error | Error as defined by swSheetSewingError_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Modeler\Modeler__CreateBodiesFromSheets.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Modeler_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\Modeler\Modeler__CreateBodiesFromSheets.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
