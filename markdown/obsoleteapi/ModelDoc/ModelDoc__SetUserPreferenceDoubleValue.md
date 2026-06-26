---
title: "ModelDoc::SetUserPreferenceDoubleValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUserPreferenceDoubleValue.htm"
---

# ModelDoc::SetUserPreferenceDoubleValue

This method is obsolete
and has been superseded by[ModelDoc2::SetUserPreferenceDoubleValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceDoubleValue.htm).

Description

This method sets various user preference values for this ModelDoc object.
This method is intended for user preferences of type double.

Syntax (OLE Automation)

retval = ModelDoc.SetUserPreferenceDoubleValue
( userPreferenceValue, value)

(Table)=========================================================

| Input: | (long) userPreferenceValue | User preference value you wish to get as defined in swUserPreferenceDoubleValue_e |
| --- | --- | --- |
| Input: | (double) value | Numeric value you wish to give to the user preference specified in userPreferenceValue |
| Return: | (BOOL) retval | TRUE if the user preference was set successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetUserPreferenceDoubleValue
( userPreferenceValue, value, &retval )

(Table)=========================================================

| Input: | (long) userPreferenceValue | User preference value you wish to get as defined in swUserPreferenceDoubleValue_e |
| --- | --- | --- |
| Input: | (double) value | the numeric value you wish to give to the user preference specified
in userPreferenceValue |
| Output: | (VARIANT_BOOL) retval | TRUE if the user preference was set successfully, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is equivalent to using theTools, Optionsmenu item in SolidWorks.

To use this method, choose one of the available
items from the swUserPreferenceDoubleValue_e enumeration.Then call this method and pass in the desired user preference from
the swUserPreferenceDoubleValue_e enumeration and the desired value for
that user preference.

For a description of the user preference
types and the types supported by each object, seekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUserPreferenceDoubleValue_e.

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
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__SetUserPreferenceDoubleValue.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="Items" value="ZExample_Get_Excel_Cell_Value_for_Density_VB$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__SetUserPreferenceDoubleValue.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
