---
title: "PartDoc::GetMaterialPropertyName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__GetMaterialPropertyName.htm"
---

# PartDoc::GetMaterialPropertyName

This method is obsolete and has been superseded
by[PartDoc::GetMaterialPropertyName2](sldworksAPI.chm::/PartDoc/PartDoc__GetMaterialPropertyName2.htm).

Description

This method gets the names
of the material database and the material.

Syntax (OLE Automation)

retval = PartDoc.GetMaterialPropertyName (*database)

(Table)=========================================================

| Output: | (BSTR *) *database | Name of material database |
| --- | --- | --- |
| Output: | (BSTR*) retval | Name of material |

Syntax (COM)

status = PartDoc->GetMaterialPropertyName ( *database,
&retval)

Parameters Table Start

(Table)=========================================================

| Output: | (BSTR *) *database | Names of material database |
| --- | --- | --- |
| Output: | (BSTR*) retval | Name of material |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If no material was applied to the part, then database
and retval are blank.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\PartDoc\PartDoc__GetMaterialPropertyName.htm" >
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
<param name="Items" value="PartDoc_Object$$**$$PartDocMaterialPropertyName$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\PartDoc\PartDoc__GetMaterialPropertyName.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
