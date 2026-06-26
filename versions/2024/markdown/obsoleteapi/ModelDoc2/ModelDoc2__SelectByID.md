---
title: "ModelDoc2::SelectByID"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__SelectByID.htm"
---

# ModelDoc2::SelectByID

This
method is obsolete and has been superseded by ModelDocExtension::SelectByID .

Description

This is a generic method for all selections in the system. With appropriate
input, it selects features, faces, edges, sketch items, and so on, at
the location specified.

Syntax (OLE Automation)

retval = ModelDoc2.SelectByID ( objectName,
objectType, x, y, z)

(Table)=========================================================

| Input: | (BSTR) objectName | Name of object to select or an empty string |
| --- | --- | --- |
| Input: | (BSTR) objectType | Type of object or an empty string (uppercase) |
| Input: | (double) x | X Selection location, or 0, see below |
| Input: | (double) y | Y Selection location, or 0, see below |
| Input: | (double) z | Z Selection location, or 0, see below |
| Return: | (BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->SelectByID (
objectName, objectType, x, y, z, &retval )

(Table)=========================================================

| Input: | (BSTR) objectName | Name of object to select or an empty string |
| --- | --- | --- |
| Input: | (BSTR) objectType | Type of object or an empty string (uppercase) |
| Input: | (double) x | X Selection location, or 0, see below |
| Input: | (double) y | Y Selection location, or 0, see below |
| Input: | (double) z | Z Selection location, or 0, see below |
| Output: | (VARIANT_BOOL) retval | TRUE if item was successfully selected, FALSE otherwise |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

Use this method instead of using the individual
selection methods on the following objects:

- Annotation
- Component2
- Feature
- SketchHatch
- SketchPoint
- SketchSegment

The previously listed objects' selection methods
do not work well when a PropertyManager page is open or a command is running.
This method, ModelDoc2::SelectByID, handles selection correctly whether
or not a command is running.

This method resets the list of selected objects
to contain only objects that match the specified criteria. To append selections
to the current selection set, see ModelDoc2::AndSelectByID.

If your application already has an object handle
(for example, Face object, SketchSegment object, and so on), see the appropriate
Select function to select the item directly using its handle.

To filter objects that get selected by ModelDoc2::SelectByID,
set the objectType argument as desired. This must be in uppercase. If
no specific type of object is required, then an empty string can be passed
in objectType; otherwise, this argument can take any of the values defined
in the comments of the enumeration swSelectType_e.

For example, to select an object of type swSelDIMENSIONS,
you should use the string that appears in the comment column, "DIMENSION".
Be aware that objectTypecanchange
based on your current state. For example, if you select a sketch point
that was created in the active sketch, then you should specify objectTypeas "SKETCHPOINT". However,
if you do not have an active sketch or if the point was created in a sketch
other than the active sketch, then you should specify the objectTypeas "EXTSKETCHPOINT".

If a type is specified in objectType, then ModelDoc2::SelectByID
returns FALSE if it cannot find the matching object type.

The objectName argument is not intended for selection
of faces, edges, and so on. This is a case-sensitive string that is intended
for objects that are automatically named during entity creation, such
as, dimensions, drawing views, and so on. ModelDoc2::SelectByID attempts
to find and select an object whose name matches the objectName string;
however, the match must be exact for it to return a value of TRUE. For
example, if a string is passed that matches an object name but whose case
does not match exactly, ModelDoc2::SelectByID may return FALSE. For selection
of dimensions, the objectName argument needs to be fully qualified. For
example you need to specify "D1@Sketch2@Part1.SLDPRT" rather
than simply "D1@Sketch2"; otherwise,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelectByID
may return FALSE. If you do not know the object name or if it is an item
that is not automatically named by SolidWorks, then you can pass an empty
string.

If you are using the objectNameparameter, then the XYZ coordinates should be in terms of the context
where the item was created. For example, if you select a sketch point
and you enter its name (for example, "Point1") in the objectName
parameter, then you should give XYZ in terms of the sketch where the point
was created. Even if the sketch is not active, the XYZ values should be
in terms of sketch space if you are using theobjectNameparameter. In
certain situations, you can also pass in the XYZ coordinates as ( 0,0,0
). For example, to select an feature shown in the FeatureManager design
tree, you do not need to give an XYZ pick location. However, to select
objects such as notes or faces or when you need a point location picked,
you must specify the XYZ coordinates.

If you are not using the objectNameparameter as a filter, then the XYZ coordinates should be in terms
of model space.

If you do not know the object name or the object
type, pass in an empty string to objectName and objectType and the selection
routine attempts to select the correct object.

To get Face, Edge or Vertex objects by name, see
PartDoc::GetEntityByName.

The ModelDoc2 object being used to call ModelDoc2::SelectByID
must be an open and visible document. For example, you cannot use the
ModelDoc2 object returned from an assembly component (for example, Component2::GetModelDoc)
unless that actual SolidWorks component part or subassembly is an open
and visible document. In this case, you could select the item using the
fully qualified name (for example, "Plane4@Part1-1@Assem1").

When selecting Face objects, the supplied point
is used as input to the normal end-user selection routines to use the
speed of ray tracing. As a result, if the view changes from the original
recorded size or orientation or both, then the same Face might not be
selected upon replay. If your application has a pointer to the Face object
to select, then you can call the Entity::Select2 method directly. Otherwise,
you can call ModelDoc2::SelectByRay. Calling ModelDoc2::SelectByRay allows
for tighter control over the starting point and the direction to search
in.

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
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__SelectByID.htm" >
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__SelectByID.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic3
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
<param name="Items" value="Feature_Suppression_Example$$**$$Plane_Creation_and_Naming_Example$$**$$Change_Note_Text_Example$$**$$Open_Assembly_Component_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\ModelDoc2\ModelDoc2__SelectByID.htm" >
<param name="_ID" value="RelatedTopic3" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
