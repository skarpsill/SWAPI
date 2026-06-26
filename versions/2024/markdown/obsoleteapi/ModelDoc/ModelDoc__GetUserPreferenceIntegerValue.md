---
title: "ModelDoc::GetUserPreferenceIntegerValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUserPreferenceIntegerValue.htm"
---

# ModelDoc::GetUserPreferenceIntegerValue

This
method is obsolete and has been superseded by[ModelDoc2::GetUserPreferenceIntegerValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceIntegerValue.htm).

Description

This method gets the specified integer user-preference
value from this document

Syntax (OLE Automation)

retval = ModelDoc.GetUserPreferenceIntegerValue (userPreferenceValue)

(Table)=========================================================

| Input: | (long) userPreferenceValue | User-preference toggle you wish to get; for a complete and up-to-date
list of available options, see swUserPreferenceIntegerValue_e |
| --- | --- | --- |
| Return: | (long) retval | Value associated with the specified userPreferenceValue setting |

Syntax (COM)

status = ModelDoc->GetUserPreferenceIntegerValue
( userPreferenceValue, &retval )

(Table)=========================================================

| Input: | (long) userPreferenceValue | User-preference toggle you wish to get; for a complete and up-to-date
list of available options, see swUserPreferenceIntegerValue_e |
| --- | --- | --- |
| Output: | (long) retval | Value associated with the specified userPreferenceValue setting |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is this same as using theTools, Optionsmenu item.

To use this method, choose one of the available
items from swUserPreferenceIntegerValue_e.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__GetUserPreferenceIntegerValue.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
