#Created April 2016
#TEASER 4 Development Team

"""buildingelement_input.py

This module contains function to load building element classes
"""

from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
import teaser.data.input.material_input as mat_input


def load_type_element(element,
                      year,
                      construction,
                      element_binding,
                      mat_binding):
    """Typical element loader.

    Loads typical building elements according to their construction
    year and their construction type from a XML. The elements are created by
    using IWU building characteristics combined with normative material data.

    This function will only work if the parents to Building are set.

    Parameters
    ----------
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER

    year : int
        Year of construction

    construction : str
        Construction type, code list ('heavy', 'light')

    element_binding : pyxb Type Element binding
        If binding is none, the Project binding will be used, otherwise you
        can use a specific XML binding for your own purpose

    mat_binding : pyxb Material binding
        If binding is none, the Project binding will be used, otherwise you
        can use a specific XML binding for your own purpose

    Raises
    ----------
    Assert if parents to Building are not set
    """
    if element_binding is None:
        ass_error_1 = "You need to specify parents for element and thermalzone"

        assert element.parent.parent.parent is not None, ass_error_1
        element_binding = element.parent.parent.parent.data.element_bind
    else:
        pass

    if mat_binding is None:
        ass_error_1 = "You need to specify parents for element and thermalzone"

        assert element.parent.parent.parent is not None, ass_error_1
        mat_binding = element.parent.parent.parent.data.material_bind
    else:
        pass
    element.year_of_construction = year

    if type(element).__name__ == 'OuterWall':

        for out_wall in element_binding.OuterWall:
            if out_wall.building_age_group[0] <= year <= \
                    out_wall.building_age_group[1] and \
                    out_wall.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=out_wall)
                for pyxb_layer in out_wall.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer,
                                    mat_binding=mat_binding)

    elif type(element).__name__ == 'InnerWall':

        for in_wall in element_binding.InnerWall:
            if in_wall.building_age_group[0] <= year <= \
                    in_wall.building_age_group[1] and \
                    in_wall.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=in_wall)
                for pyxb_layer in in_wall.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer,
                                    mat_binding=mat_binding)

    elif type(element).__name__ == 'Floor':

        for floor in element_binding.Floor:
            if floor.building_age_group[0] <= year <= \
                    floor.building_age_group[1] and \
                    floor.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=floor)
                for pyxb_layer in floor.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer,
                                    mat_binding=mat_binding)

    elif type(element).__name__ == 'Ceiling':

        for ceiling in element_binding.Ceiling:
            if ceiling.building_age_group[0] <= year <= \
                    ceiling.building_age_group[1] and \
                    ceiling.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=ceiling)
                for pyxb_layer in ceiling.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer,
                                    mat_binding=mat_binding)

    elif type(element).__name__ == 'GroundFloor':

        for gr_floor in element_binding.GroundFloor:
            if gr_floor.building_age_group[0] <= year <= \
                    gr_floor.building_age_group[1] and \
                    gr_floor.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=gr_floor)
                for pyxb_layer in gr_floor.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer,
                                    mat_binding=mat_binding)

    elif type(element).__name__ == 'Rooftop':

        for roof in element_binding.Rooftop:
            if roof.building_age_group[0] <= year <= \
                    roof.building_age_group[1] and \
                    roof.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=roof)
                for pyxb_layer in roof.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer,
                                    mat_binding=mat_binding)

    elif type(element).__name__ == 'Window':

        for win in element_binding.Window:
            if win.building_age_group[0] <= year <= \
                    win.building_age_group[1] and win.construction_type == \
                    construction:
                _set_basic_data(element=element,
                                pyxb_class=win)
                for pyxb_layer in win.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer,
                                    mat_binding=mat_binding)


def _set_layer_data(material, layer, pyxb_class, mat_binding):
    '''Helper function for load_type_element to set the layer data.

    Parameters
    ----------
    material : Material()
        Material() instance of TEASER

    layer : Layer()
        Layer() instance of TEASER

    pyxb_class :
        Pyxb class represantation of xml
    '''

    layer.thickness = pyxb_class.thickness
    layer.id = pyxb_class.id

    mat_input.load_material_id(material,
                               pyxb_class.material.material_id,
                               mat_binding)


def _set_basic_data(element, pyxb_class):
    '''Helper function for load_type_element to set the layer data.

    Parameters
    ----------
    pyxb_class :
        Pyxb class represantation of xml
    '''

    element.building_age_group = pyxb_class.building_age_group
    element.construction_type = pyxb_class.construction_type
    element.inner_radiation = pyxb_class.inner_radiation
    element.inner_convection = pyxb_class.inner_convection

    if type(element).__name__ == 'OuterWall' or \
            type(element).__name__ == 'Rooftop':
        element.inner_radiation = pyxb_class.inner_radiation
        element.inner_convection = pyxb_class.inner_convection
        element.outer_radiation = pyxb_class.outer_radiation
        element.outer_convection = pyxb_class.outer_convection

    elif type(element).__name__ == 'InnerWall' or \
            type(element).__name__ == 'Ceiling' or \
            type(element).__name__ == 'Floor' or \
            type(element).__name__ == 'GroundFloor':

        pass

    elif type(element).__name__ == 'Window':

        element.outer_radiation = pyxb_class.outer_radiation
        element.outer_convection = pyxb_class.outer_convection
        element.g_value = pyxb_class.g_value
        element.a_conv = pyxb_class.a_conv
        element.shading_g_total = pyxb_class.shading_g_total
        element.shading_max_irr = pyxb_class.shading_max_irr