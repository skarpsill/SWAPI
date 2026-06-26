---
title: "ModelDoc2::GetCustomInfoCount2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__GetCustomInfoCount2.htm"
---

# ModelDoc2::GetCustomInfoCount2

This method is obsolete and has been superseded
by[ModelDocExtension::CustomPropertyManager](sldworksAPI.chm::/ModelDocExtension/ModelDocExtension__CustomPropertyManager.htm).

Description

This method returns the number of custom information that have been
defined for either the specified configuration or for the document.

Syntax (OLE Automation)

Count = ModelDoc2.GetCustomInfoCount2
( configuration )

(Table)=========================================================

| Input: | (BSTR) configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Return: | (long) Count | Number of custom information fields |

Syntax (COM)

status = ModelDoc2->GetCustomInfoCount2
( configuration, &Count )

(Table)=========================================================

| Input: | (BSTR) configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Output: | (long) Count | Number of custom information fields |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

File custom information is stored in the document
file. It can be general to the file, in which case there is a single value
whatever the models configuration, or it can be configuration specific,
in which case a different value may be set for each configuration in the
model.

To access a general custom information value, set
the configuration argument to be an empty string.

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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__GetCustomInfoCount2.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$ModelDoc2CustomProperty$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc2\ModelDoc2__GetCustomInfoCount2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
