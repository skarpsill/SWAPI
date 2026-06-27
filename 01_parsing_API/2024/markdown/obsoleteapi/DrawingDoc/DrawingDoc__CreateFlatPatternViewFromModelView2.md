---
title: "DrawingDoc::CreateFlatPatternViewFromModelView2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateFlatPatternViewFromModelView2.htm"
---

# DrawingDoc::CreateFlatPatternViewFromModelView2

This method is obsolete and has been superseded
by[DrawingDoc::CreateFlatPatternViewFromModelView3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__CreateFlatPatternViewFromModelView3.htm).

Description

This method creates a flat-pattern view from
a model view.

Syntax (OLE Automation)

retval = DrawingDoc.CreateFlatPatternViewFromModelView2
( modelName, configName, locX, locY, locZ, hideBendLines )

(Table)=========================================================

| Input: | (BSTR) modelName | Name of model |
| --- | --- | --- |
| Input: | (BSTR) configName | Name of configuration |
| Input: | (double) locX | X coordinate |
| Input: | (double) locY | Y coordinate |
| Input: | (double) locZ | Z coordinate |
| Input: | (VARIANT_BOOL) hideBendLines | TRUE hides bend lines, FALSE does not |
| Output: | (VARIANT_BOOL) retval | TRUE if the flat-pattern view was created successfully, FALSE if it
was not |

Syntax (COM)

status = DrawingDoc->CreateFlatPatternViewFromModelView2
( modelName, configName, locX, locY, locZ, hideBendLines, &retval
)

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) modelName | Name of model |
| --- | --- | --- |
| Input: | (BSTR) configName | Name of configuration |
| Input: | (double) locX | X coordinate |
| Input: | (double) locY | Y coordinate |
| Input: | (double) locZ | Z coordinate |
| Input: | (VARIANT_BOOL) hideBendLines | TRUE hides bend lines, FALSE does not |
| Output: | (VARIANT_BOOL) retval | TRUE if the flat-pattern view was created successfully, FALSE if it
was not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic3
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__CreateFlatPatternViewFromModelView2.htm" >
<param name="_ID" value="RelatedTopic3" >
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
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\DrawingDoc\DrawingDoc__CreateFlatPatternViewFromModelView2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
