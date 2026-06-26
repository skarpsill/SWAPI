---
title: "ModelDoc::GetUserPreferenceDoubleValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUserPreferenceDoubleValue.htm"
---

# ModelDoc::GetUserPreferenceDoubleValue

This method is obsolete
and has been superseded by[ModelDoc2::GetUserPreferenceDoubleValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceDoubleValue.htm).

Description

This method gets various user preference values for this ModelDoc object.
This method is intended for user preferences of type double.

Syntax (OLE Automation)

retval = ModelDoc.GetUserPreferenceDoubleValue
( userPreferenceValue)

(Table)=========================================================

| Input: | (long) userPreferenceValue | User-preference value you wish to get; for a complete and up-to-date
list of available options, see swUserPreferenceDoubleValue_e |
| --- | --- | --- |
| Return: | (double) retval | Numeric value of the user preference specified in userPreferenceValue |

Syntax
(COM)

status = ModelDoc->GetUserPreferenceDoubleValue
( userPreferenceValue, &value )

(Table)=========================================================

| Input: | (long) userPreferenceValue | User-preference value you wish to get; for a complete and up-to-date
list of available options, see swUserPreferenceDoubleValue_e |
| --- | --- | --- |
| Output: | (double) value | Numeric value of the user preference specified in userPreferenceValue |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as selecting theTools, Optionsmenu item.

To use this method, choose one of the available
items from swUserPreferenceDoubleValue_e.The value returned is based on which user preference you are querying.

For a description of the user preference
types and the object supported by each type, seekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUserPreferenceDoubleValue_e.

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
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoUserPreference$$**$$ZModifyUserPreference$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetUserPreferenceDoubleValue.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
