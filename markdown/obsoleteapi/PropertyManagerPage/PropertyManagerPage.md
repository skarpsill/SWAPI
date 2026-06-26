---
title: "PropertyManagerPage"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage/PropertyManagerPage.htm"
---

# PropertyManagerPage

## PropertyManagerPage
Object

This
object and its methods are properties are obsolete and have been superseded
by[PropertyManagerPage2](sldworksAPI.chm::/PropertyManagerPage2/PropertyManagerPage2.htm).

(Table)=========================================================

| image\ModelDoc.gif |  |
| --- | --- |
|  | image\branch1.gif |

Allows add-in applications to display and interact with a custom PropertyManager
age that supports the look and feel of the SolidWorks PropertyManager
pages.

To use the PropertyManagerPage , follow these some guidelines:

1. Create the dialog resource with a width of 100
  dialog units and with a vertical ruler at 19 dialog units from the left,
  which should be used for positioning controls that are not flush with
  the left of the dialog. The dialog should have no title or border style.
2. PropertyManager group boxes are indicated in the
  resource by a static text control item with an ID of IDC_DVE_DIVIDER_1
  to IDC_DVE_DIVIDER_10. Size these static text control items so that they
  occupy the entire width of the dialog. The matching check boxes, if present,
  have IDs in the range IDC_DVE_DIVIDER_CHECK_1 to IDC_DVE_DIVIDER_CHECK_10.
  Use the SetGroupRange method to set the values to use for the group box
  divider static text control items and their corresponding check boxes.
  Expansion and compression of the group boxes is automatic.

For example :

(Table)=========================================================

| Dialog resource for PropertyManagerPage in Visual C++ Project | Resulting PropertyManagerPage in running SolidWorks session |
| --- | --- |
|  |  |

In the previous example, the static text
items indicate the start of a new group and the Caption property of the
static text control becomes the group title.

1. Static icons can be blended with the PropertyManager
  page background for a more finished look. To blend properly, they should
  be created as static bitmap controls, for example, window class Static
  and with the SS_BITMAP style set.

  The bitmap resource for the control is stored as a string in the dialog
  resource rather than as an ID, for example "IDB_DVE_CUBE". For
  blended icons, there should be a mask bitmap with a corresponding ID but
  appended with "_M", for example, "IDB_DVE_CUBE_M".
  If both are found, then the icon is blended, otherwise it is not.

The Second Divider Group contains an example of both blended and non-blended
icons. The upper icon is not blended; the lower icon is blended.

The add-in application must implement the IPropertyManagerPageHandler
interface, which allow you exchange dialog data with the add-in application.
This is best illustrated by the example project that can be created using
the SolidWorks Add-In AppWizard.

Use theAccessorslink to obtain a list of functions that return this object.

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
<param name="Items" value="PropertyManagerPage Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\PropertyManagerPage\PropertyManagerPage.htm" >
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc::GetPropertyManagerPage$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\PropertyManagerPage\PropertyManagerPage.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
