/// <reference types="cypress" />

describe('Test du nom de la page d \'accueil', () => {
    it('Récupère le nom de la page d\'accueil', () => {
      cy.visit('http://localhost:5000/') 
      cy.get('h1').should('contain', 'Mahamadou')
    })
  })