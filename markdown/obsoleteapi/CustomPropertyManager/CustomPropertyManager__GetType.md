---
title: "CustomPropertyManager::GetType"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomPropertyManager/CustomPropertyManager__GetType.htm"
---

# CustomPropertyManager::GetType

This method is obsolete and has been superseded
by[CustomPropertyManager::GetType2](sldworksAPI.chm::/CustomPropertyManager/CustomPropertyManager__GetType2.htm).

Description

This method gets the type
of the specified custom property.

Syntax (OLE Automation)

retval = CustomPropertyManager.GetType ( FieldName)

(Table)=========================================================

| Input: | (BSTR) FieldName | Name of the custom property whose
type to get |
| --- | --- | --- |
| Output: | (BSTR*) retval | Type of custom property |

Syntax (COM)

status = CustomPropertyManager->GetType ( FieldName,
&retval)

Parameters Table Start

(Table)=========================================================

| Input: | (BSTR) FieldName | Name of the custom property whose
type to get |
| --- | --- | --- |
| Output: | (BSTR*) retval | Type of custom property |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Type can be one of the following:

- "Text"
- "Date"
- "Number"
- "Yes or no"

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
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
<param name="Items" value="CustomPropertyManager_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\CustomPropertyManager\CustomPropertyManager__GetType.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5
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
<param name="Items" value="EXAddGetCustomProperties$$**$$EXSolidBodiesCutlistFoldersCustomProperties$$**$$EXGetCustomPropertiesCutlistItem$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\CustomPropertyManager\CustomPropertyManager__GetType.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
