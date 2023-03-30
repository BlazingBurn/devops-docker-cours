describe('Test du nom de la page d \'accueil', () => {
    it('Récupère le nom de la page d\'accueil', () => {
      cy.visit('/') 
      cy.get('h1').should('contain', 'Mahamadou')
    })
  })